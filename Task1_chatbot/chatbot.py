def chatbot(user_input):
    user_input = user_input.lower().strip()
    
    # Check for predefined questions
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! Thanks for asking."
    elif "what is your favourite animal?" in user_input:
        return "I love cats! They're so cute and clever, What about you?"
    elif "what is your favourite food?" in user_input:
        return "I enjoy virtual cookies 🍪 they never spoil!"
    elif "what are you doing?" in user_input:
        return "I'm chatting with you and learning new things every day!"
    elif "what can you do" in user_input or "help" in user_input:
        return "I can chat with you, answer questions about me, and give simple advice."
    elif "bye" in user_input:
        return "Goodbye! Have a great day."
    
    # If user input is a question but not recognized
    elif "?" in user_input:
        return "Sorry, I didn't understand that question. Can you ask something else?"
    
    # Any other statements
    else:
        return "That's nice!"

print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot:", chatbot(user_input))
        break
    print("Chatbot:", chatbot(user_input))
