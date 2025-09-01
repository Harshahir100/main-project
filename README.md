# 💻 Python Instructor Chatbot

This is a **Flask-based web application** that acts as a **Python Instructor Chatbot**.  
It uses Google's `gemini-2.5-flash` model (via `google-genai`) to answer Python-related questions.

---

## 🚀 Features
- Interactive chat interface for Python queries
- Persists chat history per user (stored in `chat_history.json`)
- History page to view all past chats
- Option to delete chat history
- Simple UI built with HTML, CSS, and JavaScript

---

## 📂 Project Structure

python-instructor-chatbot/
│── app.py # Flask backend entry point
│── requirements.txt # Python dependencies
│── chat_history.json # Stores user chat history
│── README.md # Project documentation
│
├── templates/ # HTML files (Flask Jinja2 templates)
│ ├── index.html # Main chat interface
│ └── history.html # Chat history page
│
├── static/ # Frontend assets
│ ├── css/
│ │ └── style.css # Custom styles
│ ├── js/
│ │ └── script.js # Chat functionality (AJAX)
│ └── images/ # (optional) project images/logo



---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/python-instructor-chatbot.git
cd python-instructor-chatbot


2️⃣ Create & activate a virtual environment (recommended)
python -m venv venv
# Mac/Linux
source venv/bin/activate
# Windows (cmd)
venv\Scripts\activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1

3️⃣ Install dependencies
pip install -r requirements.txt


4️⃣ Set your API key
Mac/Linux (bash/zsh):
export GENAI_API_KEY="your_api_key_here"


Windows (cmd):
set GENAI_API_KEY="your_api_key_here"


Windows (PowerShell):
$env:GENAI_API_KEY="your_api_key_here"


5️⃣ Run the Flask app
python app.py
