# Movie Night Recommender

# Welcome the user to Movie Night Recommender
print("Welcome to the Movie Night Recommender!")

# User input for mood
mood = input("How are you feeling today? (Happy, Romantic, Thrilled): ")

# Selection based on the user's mood
if mood.lower() == 'happy':
    print("For a happy mood, we recommend watching a comedy film!")
elif mood.lower() == 'romantic':
    print("Feeling romantic? A classic romantic movie is the perfect choice!")
elif mood.lower() == 'thrilled':
    print("If you're in the mood for thrills, go for an exciting action or thriller film!")
else:
    print("Not sure about your mood? We recommend a feel-good drama!")

# User input for genre preference
genre = input("Do you have a specific genre in mind? (Yes/No): ")

# Selection based on genre preference
if genre.lower() == 'yes':
    print("Great! Choose from genres like Sci-Fi, Fantasy, Drama, or Documentary for a personalized experience.")
else:
    print("No worries! We'll surprise you with a movie from a random genre.")

# Display the movie recommendation
print("Enjoy your movie night!")