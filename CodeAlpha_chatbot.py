def get_response(user_input):
    """Return a predefined reply based on user input."""
    user_input = user_input.strip().lower()

    if user_input in ("hello", "hi", "hey"):
        return "Hi! How can I help you today?"

    elif user_input in ("how are you", "how are you?", "how r u"):
        return "I'm fine, thanks! How about you?"

    elif user_input in ("i'm good", "im good", "fine", "good", "great"):
        return "That's great to hear!"

    elif user_input in ("what is your name", "what's your name", "who are you"):
        return "I'm a simple chatbot built with Python!"

    elif user_input in ("what can you do", "help", "what do you do"):
        return "I can chat with you! Try saying hello, ask how I am, or say goodbye."

    elif user_input in ("bye", "goodbye", "see you", "exit", "quit"):
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I didn't understand that. Try: hello, how are you, or bye."


def chatbot():
    print("=" * 40)
    print("       Welcome to SimpleBot!")
    print("=" * 40)
    print("Type 'bye' or 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Bot: Please type something!")
            continue

        response = get_response(user_input)
        print(f"Bot: {response}")

        # Exit condition
        if user_input.lower() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    chatbot()
