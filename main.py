import gradio as gr
import ollama
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import PyPDF2
import pandas as pd
from datetime import datetime
import os
if not os.path.exists('qa_history.csv'):
    pd.DataFrame(columns=['timestamp', 'model', 'question', 'answer']).to_csv('qa_history.csv', index=False)
AVAILABLE_MODELS = [
    "tinyllama:latest", 
    "qwen:latest", 
    "llama3.2:latest", 
    "qwen3:latest"
]
MODEL_INFO = {
    "tinyllama:latest": {"size": "637 MB", "best_for": "Fast responses"},
    "qwen:latest": {"size": "2.3 GB", "best_for": "Balanced performance"},
    "llama3.2:latest": {"size": "2.0 GB", "best_for": "High-quality answers"},
    "qwen3:latest": {"size": "5.2 GB", "best_for": "Advanced tasks"}
}
def extract_text(file):
    if file.name.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        return " ".join([page.extract_text() for page in reader.pages])
    else:
        return open(file.name).read()

def generate_wordcloud(notes):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(notes)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    return plt

def log_interaction(model, question, answer):
    new_entry = pd.DataFrame({
        'timestamp': [datetime.now()],
        'model': [model],
        'question': [question],
        'answer': [answer]
    })
    new_entry.to_csv('qa_history.csv', mode='a', header=False, index=False)

def get_stats():
    if os.path.exists('qa_history.csv'):
        df = pd.read_csv('qa_history.csv')
        total_questions = len(df)
        most_used_model = df['model'].mode()[0] if not df.empty else "N/A"
        return f"Total Questions: {total_questions}\nMost Used Model: {most_used_model}"
    return "No history yet"

def answer_question(file, question, model_name):
    try:
        notes = extract_text(file)
        prompt = f"Based on these notes: {notes}\n\nQuestion: {question}"
        response = ollama.chat(
            model=model_name,
            messages=[{'role': 'user', 'content': prompt}]
        )
        answer = response['message']['content']
        log_interaction(model_name, question, answer)
        
        return answer, generate_wordcloud(notes)
    
    except Exception as e:
        return f"Error: {str(e)}", None
with gr.Blocks(theme=gr.themes.Soft(), title="AI Study Assistant") as app:
    gr.Markdown("# 📚 AI Study Assistant")
    gr.Markdown("Upload your notes and ask questions!")
    
    with gr.Row():
        with gr.Column():
            model_dropdown = gr.Dropdown(
                choices=AVAILABLE_MODELS,
                value="tinyllama:latest",
                label="Select Model",
                interactive=True
            )
            
            model_info = gr.Markdown(
                f"**tinyllama:latest**: 637 MB - Best for: Fast responses"
            )
            
            file_input = gr.File(label="Upload Notes (PDF or TXT)")
            question_input = gr.Textbox(label="Your Question", lines=3)
            submit_btn = gr.Button("Get Answer", variant="primary")
            
            stats = gr.Markdown(get_stats())
        
        with gr.Column():
            answer_output = gr.Textbox(label="Answer", interactive=False)
            wordcloud_output = gr.Plot(label="Notes Word Cloud")
    def update_model_info(model_name):
        info = MODEL_INFO.get(model_name, {"size": "?", "best_for": "?"})
        return f"**{model_name}**: {info['size']} - Best for: {info['best_for']}"
    
    model_dropdown.change(
        update_model_info,
        inputs=model_dropdown,
        outputs=model_info
    )
    submit_btn.click(
        answer_question,
        inputs=[file_input, question_input, model_dropdown],
        outputs=[answer_output, wordcloud_output]
    )
    submit_btn.click(
        lambda: gr.Markdown(get_stats()),
        outputs=stats
    )
if __name__ == "__main__":
    app.launch()