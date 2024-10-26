# -*- coding: utf-8 -*-
"""
  
********
Shan Marky Isidro
"""
# I add the list of the countries and capitals
questions = [
    ("France", "Paris"),
    ("Albania", "Tirana"),
    ("Austria", "Vienna"),
    ("Spain", "Madrid"),
    ("Croatia", "Zagreb"),
    ("Cyprus", "Nicosia"),
    ("Belgium", "Brussels"),
    ("Greece", "Athens"),
    ("Norway", "Oslo"),
    ("United Kingdom", "London")
]
# I ask the user for the capital of france
answer = input("What is the capital of France? ").strip()
# It will show if the answer is correct or wrong
if answer.lower() == "paris":  # Ignore capitalization
    print("Correct! The capital of France is Paris.")
else:
    print("Wrong! The capital of France is Paris.")
    print("\nNow, let's quiz you on the capitals of 10 European countries!")
score = 0  # It initialize the score
# I use Loop for the countries and capitals
for country, capital in questions:
    answer = input(f"What is the capital of {country}? ").strip()
    if answer.lower() == capital.lower():  # Ignore capitalization
        print("Correct!")
        score += 1  # Increment score for a correct answer
    else:
        print(f"Wrong! The capital of {country} is {capital}.")
# It will show the result of the score
        print(f"\nYour final score is {score} out of {len(questions)}.")
