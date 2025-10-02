print("Welcome to CODSOFT AI Projects App")
print("Choose a project to run:")
print("1. Chatbot")
print("2. Tic-Tac-Toe AI")
print("3. Recommendation System")
print("4. Exit")

while True:
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        try:
            with open("Task1_Chatbot/chatbot.py", encoding="utf-8") as f:
                exec(f.read())
        except FileNotFoundError:
            print("Chatbot file not found. Make sure Task1_Chatbot/chatbot.py exists.")
    elif choice == "2":
        try:
            with open("Task2_TicTacToe/tictactoe.py", encoding="utf-8") as f:
                exec(f.read())
        except FileNotFoundError:
            print("Tic-Tac-Toe file not found. Make sure Task2_TicTacToe/tictactoe.py exists.")
    elif choice == "3":
        try:
            with open("Task3_RecommendationSystem/recommendation.py", encoding="utf-8") as f:
                exec(f.read())
        except FileNotFoundError:
            print("Recommendation System file not found. Make sure Task3_RecommendationSystem/recommendation.py exists.")
    elif choice == "4":
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
