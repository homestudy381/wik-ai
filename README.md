from flask import Flask, render_template_string, request, redirect, url_for, session
import math

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Login credentials
USERNAME = "HORICK"
SECRET_CODE = "WILLIAX256"

# Knowledge base
knowledge = {
    "who created you": "I was created by WIKBOYZ Eugene.",
    "what is your name": "I am WIK AI 2026.",
    "hello": "Hi! I am WIK AI 2026, created by WIKBOYZ Eugene. How can I help you?",
    "hi": "Hi! I am WIK AI 2026, created by WIKBOYZ Eugene. How can I help you?",
    "who is the president of usa": "The current president of the USA is Joe Biden (as of 2025).",
    "what is africa": "Africa is the second-largest continent in the world, with 54 countries."
}

# Helper: check if logged in
def is_logged_in():
    return "logged_in" in session and session["logged_in"]

# Login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        code = request.form["code"]
        if username.upper() == USERNAME and code.upper() == SECRET_CODE:
            session["logged_in"] = True
            return redirect(url_for("chat"))
        else:
            return "<h3>Wrong name or code! Try again.</h3>"
    return '''
        <h1>🔐 Welcome to WIK AI 2026</h1>
        <form method="post">
            Name: <input type="text" name="username"><br><br>
            Code: <input type="password" name="code"><br><br>
            <input type="submit" value="Enter">
        </form>
    '''

# Chat page
@app.route("/chat", methods=["GET", "POST"])
def chat():
    if not is_logged_in():
        return redirect(url_for("login"))
    
    response = ""
    if request.method == "POST":
        user_input = request.form["message"].lower()
        try:
            # Math calculation
            if "calculate" in user_input:
                expr = user_input.replace("calculate", "").strip()
                result = eval(expr, {"__builtins__": None}, math.__dict__)
                response = f"The result is {result}"
            elif user_input in knowledge:
                response = knowledge[user_input]
            else:
                response = "I don't know that yet. I am still learning."
        except Exception:
            response = "Sorry, I couldn't calculate that."

    return render_template_string('''
        <h2>🤖 WIK AI 2026 Chat</h2>
        <form method="post" id="chat-form">
            <input type="text" name="message" placeholder="Ask me anything..." style="width:300px" id="user-input">
            <input type="submit" value="Send">
        </form>
        <p><b>WIK AI:</b> <span id="response">{{response}}</span></p>

        <script>
            var responseText = "{{response}}";
            if(responseText){
                var msg = new SpeechSynthesisUtterance(responseText);
                window.speechSynthesis.speak(msg);
            }

            document.getElementById("chat-form").onsubmit = function() {
                setTimeout(function(){document.getElementById("user-input").focus();}, 100);
            };
        </script>
    ''', response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
