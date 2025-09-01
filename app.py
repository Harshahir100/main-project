import os
import json
from datetime import datetime
from flask import Flask, request, render_template, jsonify
from google import genai
from google.genai import types

# Read API key
api_key = os.getenv("GENAI_API_KEY")
if not api_key:
    raise ValueError("Missing GENAI_API_KEY environment variable. Set it before running the script.")

client = genai.Client(api_key=api_key)
app = Flask(__name__)

# File to store chat history
CHAT_HISTORY_FILE = "chat_history.json"

def load_chat_history():
    """Load chat history from file"""
    if os.path.exists(CHAT_HISTORY_FILE):
        try:
            with open(CHAT_HISTORY_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_chat_history(chat_history):
    """Save chat history to file"""
    with open(CHAT_HISTORY_FILE, 'w') as f:
        json.dump(chat_history, f, indent=2)

def format_python_response(text: str) -> str:
    """Wrap Python-looking code blocks with ```python formatting"""
    if "```" in text:
        return text
    formatted = []
    in_code = False
    for line in text.splitlines():
        if line.strip().startswith(("def ", "class ", "import ", "from ", "#", "for ", "if ", "elif ", "else:", "print(")):
            if not in_code:
                formatted.append("```python")
                in_code = True
            formatted.append(line)
        else:
            if in_code:
                formatted.append("```")
                in_code = False
            formatted.append(line)
    if in_code:
        formatted.append("```")
    return "\n".join(formatted)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_query = request.form.get("query")
    session_id = request.remote_addr  # Using IP as session ID

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_query,
        config=types.GenerateContentConfig(
            system_instruction="""You are a Python Instructor.
You will only reply to problems related to Python (Core Python, Advanced Python, OOPs, NumPy, Pandas, Django, Flask, PyTorch).
You have to solve queries in the simplest way with clear examples.

IMPORTANT: Format your responses with clear line breaks. Use triple backticks (```python) to wrap code examples.
Make sure your explanations are well-structured with proper paragraph breaks.

If the user asks any question which is not related to Python, reply rudely.
Example: If the user asks "How are you?"
You will reply: "You dumb, ask me some sensible Python question."
(You can be even more rude if you like.)

If the question is about Python or the listed topics, reply politely with a simple explanation and example.
"""
        ),
    )

    # Extract text from response
    answer_text = response.candidates[0].content.parts[0].text
    formatted_response = format_python_response(answer_text)

    # Save to chat history
    chat_history = load_chat_history()
    current_date = datetime.now().strftime("%Y-%m")

    if session_id not in chat_history:
        chat_history[session_id] = {}
    if current_date not in chat_history[session_id]:
        chat_history[session_id][current_date] = []

    chat_history[session_id][current_date].append({
        "timestamp": datetime.now().isoformat(),
        "query": user_query,
        "response": formatted_response
    })

    save_chat_history(chat_history)
    return jsonify({"answer": formatted_response})

@app.route("/history")
def history():
    """Render history in HTML"""
    session_id = request.remote_addr
    chat_history = load_chat_history()
    session_history = chat_history.get(session_id, {})

    history_list = []
    for month, conversations in session_history.items():
        title = conversations[0]["query"][:50] + "..." if len(conversations[0]["query"]) > 50 else conversations[0]["query"]
        history_list.append({
            "month": month,
            "title": title,
            "count": len(conversations),
            "conversations": conversations
        })

    history_list.sort(key=lambda x: x["month"], reverse=True)
    return render_template("history.html", history=history_list)

@app.route("/history/json")
def history_json():
    """Return history as JSON"""
    session_id = request.remote_addr
    chat_history = load_chat_history()
    return jsonify(chat_history.get(session_id, {}))

@app.route("/delete-history", methods=["POST"])
def delete_history():
    session_id = request.remote_addr
    chat_history = load_chat_history()
    if session_id in chat_history:
        del chat_history[session_id]
        save_chat_history(chat_history)
        return jsonify({"status": "success"})
    return jsonify({"status": "no history found"})

if __name__ == "__main__":
    app.run(debug=True)
