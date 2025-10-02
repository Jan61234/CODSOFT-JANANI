
users = {
    "Alice": ["Harry Potter", "Inception", "Avengers"],
    "Bob": ["Inception", "Avengers", "Titanic"],
    "Charlie": ["Harry Potter", "Titanic", "Joker"]
}

# Function to get recommendations
def recommend(user_name, user_items):
    recommendations = []
    for other_user, items in users.items():
        for item in items:
            if item not in user_items:
                recommendations.append(item)
    recs = set(recommendations)
    if recs:
        print(f"\nRecommendations for {user_name}: {recs}")
    else:
        print(f"\nNo new recommendations available for {user_name}.")

# Main program
print("Welcome to the Recommendation System!\n")
user_name = input("Enter your name: ")

# Let user enter their preferences
print("\nEnter your items of interest one by one. Type 'done' when finished:")
user_items = []
while True:
    item = input("Item: ")
    if item.lower() == "done":
        break
    if item.strip() != "":
        user_items.append(item.strip())

# Show recommendations
recommend(user_name, user_items)
