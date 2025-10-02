users = {
    "Alice": ["Harry Potter", "Inception", "Avengers"],
    "Bob": ["Inception", "Avengers", "Titanic"],
    "Charlie": ["Harry Potter", "Titanic", "Joker"]
}

def recommend(user):
    if user not in users:
        print(f"Sorry, we don't have data for {user}.")
        return
    recommendations = []
    for other_user, items in users.items():
        if other_user != user:
            for item in items:
                if item not in users[user]:
                    recommendations.append(item)
    recs = set(recommendations)
    if recs:
        print(f"Recommendations for {user}: {recs}")
    else:
        print(f"No new recommendations available for {user}.")

# Ask for user input
user_name = input("Enter your name: ")
recommend(user_name)
