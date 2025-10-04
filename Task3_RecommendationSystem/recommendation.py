
users = {
    "Alice": ["Harry Potter", "Inception", "Avengers"],
    "Bob": ["Inception", "Avengers", "Titanic"],
    "Charlie": ["Harry Potter", "Titanic", "Joker"],
    "David": ["Joker", "Inception", "Interstellar"]
}

# Function to calculate similarity between two users
def calculate_similarity(user_items, other_items):
    common = set(user_items) & set(other_items)
    return len(common)

# Function to recommend items based on most similar user
def recommend(user_name, user_items):
    most_similar_user = None
    max_similarity = 0

    for other_user, items in users.items():
        if other_user == user_name:
            continue
        similarity = calculate_similarity(user_items, items)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_user = other_user

    if most_similar_user:
        similar_user_items = set(users[most_similar_user])
        new_recommendations = similar_user_items - set(user_items)

        if new_recommendations:
            print(f"\n Recommendations for {user_name} (based on {most_similar_user}'s preferences):")
            for rec in new_recommendations:
                print(f" - {rec}")
        else:
            print(f"\n {user_name}, you’ve already seen what {most_similar_user} likes! No new recommendations.")
    else:
        print(f"\n⚠️ No similar users found. Try adding more preferences!")

# -------------------------------
# Main Program
# -------------------------------
print(" Welcome to the Smart Movie Recommendation System!\n")
user_name = input("Enter your name: ")

# Collect user preferences
print("\nEnter your favorite movies one by one. Type 'done' when finished:")
user_items = []
while True:
    item = input("Movie: ")
    if item.lower() == "done":
        break
    if item.strip() != "":
        user_items.append(item.strip())

# Save this user into dataset (optional)
users[user_name] = user_items

# Generate recommendations
recommend(user_name, user_items)

