from flask import Flask, render_template_string, request, session, redirect, url_for
import math

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this to your own secret

# Security code for login
SECURITY_CODE = "12345"

# Knowledge base
knowledge = {
    "who created you": "I was created by WIKBOYZ Eugene.",
    "what is your name": "I am WIK-AI 2025.",
    "hello": "Hi! I am WIK-AI 2025, created by WIKBOYZ Eugene. How can I help you?",
    "hi": "Hi! I am WIK-AI 2025, created by WIKBOYZ Eugene. How can I help you?",
    "who is the president of usa": "The current president of the USA is Joe Biden (as of 2025).",
    "what is africa": "Africa is the second-largest continent in the world, with 54 countries.",
    "what is algebra": "Algebra is a branch of mathematics dealing with symbols and rules for manipulating those symbols.",
    "what is biology": "Biology is the study of living organisms, their structure, function, growth, and evolution."
}

def is_logged_in():
    return "logged_in" in session and session["logged_in"]

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        code = request.form.get("code")
        if code == SECURITY_CODE:
            session["logged_in"] = True
            return redirect(url_for("chat"))
        else:
            return "<h3>Wrong security code!</h3>"
    return '''
        <h2>🔐 WIK-AI 2025 Login</h2>
        <form method="post">
            Security Code: <input type="password" name="code">
            <input type="submit" value="Login">
        </form>
    '''

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if not is_logged_in():
        return redirect(url_for("login"))

    response = ""
    user_input = ""

    if request.method == "POST":
        user_input = request.form.get("message").strip()
        try:
            if "calculate" in user_input.lower():
                expr = user_input.lower().replace("calculate", "").strip()
                result = eval(expr, {"__builtins__": None}, math.__dict__)
                response = f"The result is {result}"
            elif user_input.lower() in knowledge:
                response = knowledge[user_input.lower()]
            else:
                response = "I don't know that yet. I am still learning."
        except:
            response = "Sorry, I couldn't calculate that."

    return render_template_string('''
        <!doctype html>
        <html>
        <head>
            <title>WIK-AI 2025 Chat</title>
            <style>
                body { font-family: Arial; background: #f5f5f5; display: flex; flex-direction: column; align-items: center; }
                .chat-box { width: 400px; max-height: 500px; background: #fff; border-radius: 10px; padding: 10px; overflow-y: auto; margin-top: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
                .bubble { padding: 10px; border-radius: 15px; margin: 5px 0; max-width: 80%; }
                .user { background: #4CAF50; color: #fff; margin-left: auto; text-align: right; }
                .bot { background: #e0e0e0; color: #000; margin-right: auto; text-align: left; }
                form { display: flex; margin-top: 10px; }
                input[type=text] { flex: 1; padding: 10px; border-radius: 20px; border: 1px solid #ccc; }
                input[type=submit] { padding: 10px 20px; margin-left: 5px; border-radius: 20px; background: #4CAF50; color: white; border: none; cursor: pointer; }
            </style>
        </head>
        <body>
            <h2>🤖 WIK-AI 2025</h2>
            <div class="chat-box" id="chat-box">
                {% if user_input %}
                    <div class="bubble user">{{ user_input }}</div>
                    <div class="bubble bot">{{ response }}</div>
                {% else %}
                    <div class="bubble bot">Hi! I am WIK-AI 2025. Ask me anything!</div>
                {% endif %}
            </div>
            <form method="post">
                <input type="text" name="message" placeholder="Type your question..." autofocus>
                <input type="submit" value="Send">
            </form>
            <script>
                // Scroll to the bottom on new messages
                var chatBox = document.getElementById("chat-box");
                chatBox.scrollTop = chatBox.scrollHeight;

                // Optional text-to-speech
                {% if response %}
                var msg = new SpeechSynthesisUtterance("{{ response }}");
                window.speechSynthesis.speak(msg);
                {% endif %}
            </script>
        </body>
        </html>
    ''', user_input=user_input, response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True) import random
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Knowledge base
knowledge = {
    "math": {
        "What is 2 + 2?": "2 + 2 equals 4.",
        "What is 5 times 3?": "5 times 3 equals 15."
    },
    "science": {
        "What is the chemical symbol for water?": "The chemical symbol for water is H2O.",
        "What planet is known as the Red Planet?": "Mars is known as the Red Planet."
    },
    "history": {
        "Who was the first president of the United States?": "George Washington was the first president of the United States.",
        "In what year did World War II end?": "World War II ended in 1945."
    }
}

# Function to get a random question and answer
def get_random_qa():
    category = random.choice(list(knowledge.keys()))
    question, answer = random.choice(list(knowledge[category].items()))
    return question, answer

# Function to speak the answer
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main function
def main():
    print("Welcome to WIK-AI 2025!")
    while True:
        question, answer = get_random_qa()
        print(f"Question: {question}")
        print(f"Answer: {answer}")
        speak(answer)
        user_input = input("Press Enter to get another Q&A or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            break

if __name__ == "__main__":
    main()
    app.run(host="0.0.0.0", port=5000)Update WIK AI 2025 with new knowledgeAdded new responses for math, science, history, and enabled text-to-speech support for WIKAI 2025.
