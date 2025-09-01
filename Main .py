from flask import Flask, render_template_string, request, redirect, url_for, session
import pyttsx3

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this to your own secret

# Security code
SECURITY_CODE = "12345"

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Knowledge base
knowledge = {
    "who created you": "I was created by WIKBOYZ Eugene.",
    "what is your name": "I am WIK AI 2025.",
    "hello": "Hi! I am WIK AI 2025. How can I help you?",
    "hi": "Hi! I am WIK AI 2025. How can I help you?",
    "who is the president of usa": "The current president of the USA is Joe Biden (as of 2025).",
    "what is africa": "Africa is the second-largest continent in the world, with 54 countries."
}

# Helper function to check login
def is_logged_in():
    return "logged_in" in session and session["logged_in"]

# Login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        code = request.form["code"]
        if code == SECURITY_CODE:
            session["logged_in"] = True
            return redirect(url_for("home"))
        else:
            return "Wrong security code!"
    return """
    <h2>🔐 WIK AI 2025 Login</h2>
    <form method="post">
        Security Code: <input type="password" name="code">
        <input type="submit" value="Login">
    </form>
    """

# Home page
@app.route("/home")
def home():
    if not is_logged_in():
        return redirect(url_for("login"))
    return """
    <h1>Welcome to WIK AI 2025</h1>
    <p>Visit <a href='/wiki'>Wiki Page</a> to learn more about me.</p>
    <p>Visit <a href='/chat'>Chat with WIK AI</a> to ask questions.</p>
    """

# Wiki page
@app.route("/wiki")
def wiki():
    if not is_logged_in():
        return redirect(url_for("login"))
    return """
    <h1>WIK AI 2025 Wiki</h1>
    <ul>
        <li>Name: WIK AI 2025</li>
        <li>Creator: WIKBOYZ Eugene</li>
        <li>Capabilities: Chat, Answer Questions, Speak Text</li>
    </ul>
    <p>Go back to <a href='/home'>Home</a></p>
    """

# Chat page
@app.route("/chat", methods=["GET", "POST"])
def chat():
    if not is_logged_in():
        return redirect(url_for("login"))

    response = ""
    if request.method == "POST":
        user_input = request.form["message"].lower()
        if user_input in knowledge:
            response = knowledge[user_input]
        else:
            response = "I don't know that yet. I am still learning."

        # Speak the response
        engine.say(response)
        engine.runAndWait()

    return render_template_string("""
        <h1>Chat with WIK AI 2025</h1>
        <form method="post">
            <input type="text" name="message" placeholder="Ask me anything..." style="width:300px">
            <input type="submit" value="Send">
        </form>
        <p><b>WIK AI:</b> {{response}}</p>
        <p>Go back to <a href='/home'>Home</a></p>
    """, response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)Update WIK AI 2025 with new knowledgeAdded new responses for math, science, history, and enabled text-to-speech support for WIKAI 2025.
