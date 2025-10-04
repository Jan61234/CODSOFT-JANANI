

# Preference-Based Movie Recommendation System


# Predefined preference categories
preferences = {
    "Preference 1": ["Harry Potter", "Fantastic Beasts", "Percy Jackson", "The Hobbit"],
    "Preference 2": ["Inception", "Interstellar", "Tenet", "The Prestige"],
    "Preference 3": ["Avengers", "Iron Man", "Captain America", "Thor"],
    "Preference 4": ["Titanic", "The Notebook", "La La Land", "P.S. I Love You"],
    "Preference 5": ["Joker", "Fight Club", "The Dark Knight", "Gone Girl"]
}

print(" Welcome to the Smart Movie Recommendation System!\n")
print("We’ll recommend movies similar to your interests.")

# Step 1: Ask for user input
user_name = input("\nEnter your name: ")
print("\nEnter your favorite movies one by one (type 'done' when finished):")

user_movies = []
while True:
    movie = input("Movie: ").strip()
    if movie.lower() == "done":
        break
    if movie:
        user_movies.append(movie)

# Step 2: Generate recommendations
recommendations = set()

for movie in user_movies:
    for pref_name, movie_list in preferences.items():
        if movie in movie_list:
            # Add other movies from same preference
            for m in movie_list:
                if m not in user_movies:
                    recommendations.add(m)

# Step 3: Display results
if recommendations:
    print(f"\n {user_name}, based on your preferences, you might enjoy:")
    for rec in recommendations:
        print(f" - {rec}")
else:
    print(f"\n⚠️ Sorry {user_name}, we couldn’t find any similar movies. Try entering popular titles next time!")

print("\n Thank you for using the Recommendation System!")
