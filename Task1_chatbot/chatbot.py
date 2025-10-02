def chatbot(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! Thanks for asking."
    elif "bye" in user_input:
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I didn't understand that."

print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot:", chatbot(user_input))
        break
    print("Chatbot:", chatbot(user_input))
