# Objective: Utilize conditional statements to guide program execution based on user input regarding weather conditions.
# Task Description: Create a Python script named weather_advice.py.
# This script will ask the user about the current weather conditions and provide clothing recommendations based on the input.
# This task aims to demonstrate the use of if, elif, and else statements to make decisions in a program.
# File: weather_advice.py
# Directory: control-flow
# Repository: alx_be_python

def provide_weather_advice():
    """
    Asks the user for current weather conditions and provides clothing recommendations.
    Ensures exact matching for prompts, conditions, and outputs as required by checks.
    """
    # 1. Prompt User for Weather Input:
    # Use the prompt: What's the weather like today? (sunny/rainy/cold):
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower() # Changed variable name to 'weather'

    # 2. Provide Clothing Recommendations:
    # Based on the user’s input, your program will recommend different types of clothing:
    if weather == "sunny": # Using 'weather' variable
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy": # Using 'weather' variable
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold": # Using 'weather' variable
        print("Make sure to wear a warm coat and a scarf.")
    else:
        # Include an else statement that handles unexpected input by printing:
        print("Sorry, I don't have recommendations for this weather.")

# Call the function to run the script
if __name__ == "__main__":
    provide_weather_advice()

