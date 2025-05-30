# AI Study Assistant with Local LLMs 🚀
*A smart study companion powered by local LLMs (TinyLlama, Qwen, Llama3) that answers questions from your notes.*
## Features ✨
- **Multi-Model Support**: Choose between different local LLMs (TinyLlama, Qwen, Llama3.2, Qwen3)
- **Document Processing**: Upload PDF or TXT lecture notes
- **Intelligent Q&A**: Get accurate answers based on your study materials
- **Visual Analytics**: 
  - Word cloud generation from notes
  - Usage statistics tracking
- **Privacy-First**: All processing happens locally via Ollama
- **Conversation History**: Automatic logging of all Q&A sessions

## Tech Stack 🛠️

| Component               | Technology Used |
|-------------------------|----------------|
| Local LLMs              | Ollama (TinyLlama, Qwen, Llama3) |
| Backend                 | Python 3.10+   |
| Web Interface           | Gradio         |
| PDF Processing          | PyPDF2         |
| Text Analysis           | WordCloud, NLTK|
| Data Management         | Pandas         |

## Installation Guide 💻

### Prerequisites
- Windows/Linux/Mac
- Python 3.10+
- Ollama installed ([Installation Guide](https://ollama.ai/))

### Setup Steps
Download your preferred LLM models (run in PowerShell/terminal):

bash
ollama pull tinyllama
ollama pull qwen
ollama pull llama3.2
Clone this repository:

bash
git clone https://github.com/yourusername/ai-study-assistant.git
cd ai-study-assistant
Run the application:

bash
python study_assistant.py
Access the web interface at http://127.0.0.1:7860

Usage Guide 📖
Upload your notes (PDF or TXT format)

Select a model based on your needs:

🚀 TinyLlama: Fastest responses

⚖️ Qwen: Balanced performance

🧠 Llama3.2: Highest accuracy

Ask questions about your study material

Explore features:

View word clouds of key concepts

Check your question history

Compare model performance

Project Structure 📂
ai-study-assistant/
├── study_assistant.py      # Main application code
├── qa_history.csv          # Auto-generated question log
├── requirements.txt        # Python dependencies
└── README.md               # This documentation
Future Enhancements 🔮
Add voice input/output support

Implement follow-up question handling

Add multilingual support

Deploy as web application

Contributing 🤝
Contributions are welcome! Please open an issue or submit a PR for any:

Bug fixes

New features

Documentation improvements

License 📜
This project is licensed under the MIT License - see the LICENSE file for details.

Created by Pratik ! - Feel free to connect on LinkedIn!

1. **Install required Python packages**:
   ```bash
   pip install gradio ollama PyPDF2 wordcloud pandas matplotlib
