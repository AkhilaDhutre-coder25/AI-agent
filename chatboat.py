import time

def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    
    # Greetings
    if user_input in ['hi', 'hello', 'hey', 'greetings']:
        return "Hello! How can I assist you today?"
    
    # Identity inquiries
    elif "who are you" in user_input or "your name" in user_input:
        return "I am AI Assistant, a college project chatbot designed to help answer your questions!"
    
    # Help & Capabilities
    elif "what can you do" in user_input or "help" in user_input:
        return "I can answer basic questions, greet users, and assist with general inquiries. Try asking me about college, project details, or just say hi!"
    
    # College related queries
    elif "college" in user_input or "university" in user_input:
        return "Colleges are institutions of higher learning! This chatbot was developed as part of a computer science project."
    
    # Farewell
    elif user_input in ['bye', 'goodbye', 'see you', 'exit', 'quit']:
        return "Goodbye! Have a great day ahead!"
    
    # Default fallback response
    else:
        return "I'm sorry, I didn't quite understand that. Could you please rephrase your question?"

def main():
    print("=" * 50)
    print("      WELCOME TO AI CHATBOT SYSTEM      ")
    print("   (Type 'exit' or 'bye' to stop the chat)  ")
    print("=" * 50)
    time.sleep(0.5)

    while True:
        try:
            user_input = input("\nYou: ")
            if not user_input.strip():
                continue
                
            if user_input.lower().strip() in ['exit', 'bye', 'quit']:
                print("Bot: Goodbye! Have a great day!")
                break
                
            response = get_bot_response(user_input)
            print(f"Bot: {response}")
            
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Session ended. Goodbye!")
            break

if __name__ == "__main__":
    main()