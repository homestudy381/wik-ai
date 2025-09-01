 import random
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
