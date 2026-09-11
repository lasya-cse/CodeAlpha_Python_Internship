def display_header():
    print("\n"+"="*50)
    print("              BASIC CHATBOT")
    print("="*50)
    print("Type 'bye' to end the conversation.")
    print("="*50)
def get_response(user_input):
    user_input=user_input.lower().strip()
    if user_input=="hello" or user_input=="hi" or user_input=="hey":
        return "Hi! How can I help you?"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "what is your name" in user_input or "your name" in user_input:
        return "I'm a Basic Python Chatbot."
    elif "who are you" in user_input:
        return "I am a simple rule-based chatbot created using Python."
    elif "help" in user_input:
        return "Sure! You can say hello, ask how I am, or say bye."
    elif user_input=="bye" or user_input=="goodbye":
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that. Please try another message."
def chatbot():
    display_header()
    while True:
        user_input=input("\nYou: ").strip()
        if not user_input:
            print("Bot: Please enter a message.")
            continue
        response=get_response(user_input)
        print("Bot:",response)
        if user_input.lower()=="bye" or user_input.lower()=="goodbye":
            break
def main():
    chatbot()
if __name__=="__main__":
    main()
