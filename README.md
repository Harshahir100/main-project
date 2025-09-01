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

2️⃣ Create & activate a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\\Scripts\\activate    # Windows


3️⃣ Install dependencies
pip install -r requirements.txt


4️⃣ Set your API key
export GENAI_API_KEY="your_api_key_here"   # Mac/Linux
set GENAI_API_KEY="your_api_key_here"      # Windows (cmd)
$env:GENAI_API_KEY="your_api_key_here"     # Windows (PowerShell)


5️⃣ Run the Flask app
python app.py







