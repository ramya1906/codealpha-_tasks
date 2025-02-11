def chatbot():
    print("Hello! I am a simple chatbot. Type 'exit' to end.")
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        elif "hello" in user_input:
            print("Chatbot: Hi there!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great!")
        elif "your name" in user_input:
            print("Chatbot: I am ChatBot 1.0.")
        else:
            print("Chatbot: Sorry, I don't understand.")

chatbot()
