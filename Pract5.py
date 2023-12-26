#  Design a Python program for creating a Random story generator

import random

def generate_random_story():
    # Lists of possible story elements
    characters = ['Roshini', 'Akanksha', 'Karan', 'Kiran']
    locations = ['the forest', 'a mysterious castle', 'a futuristic city', 'an ancient village']
    actions = ['confessed her love for me..karan😊', 'solved a mystery of omnitrix', 'travelling the world', 'saved the day']

    # Generate a random story
    character = random.choice(characters)
    location = random.choice(locations)
    action = random.choice(actions)

    print(f"Once upon a time, {character} found themselves in {location}. They {action}!")
   # Print the generated story

# Call the function to generate a random story..
generate_random_story()
