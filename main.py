print("Welcome to CODSOFT AI Projects App")
print("Choose a project to run:")
print("1. Chatbot")
print("2. Tic-Tac-Toe AI")
print("3. Recommendation System")
print("4. Exit")
while True:
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        import Task1_Chatbot.chatbot
    elif choice == "2":
        import Task2_TicTacToe.tictactoe
    elif choice == "3":
        import Task3_RecommendationSystem.recommendation
    elif choice == "4":
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
