# Let's create a README.md file with setup and run instructions for the project
readme_content = """# 💻 Python Instructor Chatbot

This is a Flask-based web application that acts as a **Python Instructor** chatbot.  
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


python-instructor-chat/
│── app.py # Flask backend
│── chat_history.json # Stores chat history (auto-created)
│── requirements.txt # Dependencies
│── README.md # Project documentation
│
├── templates/
│ ├── index.html # Main chat interface
│ └── history.html # Chat history page

