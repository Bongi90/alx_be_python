# Objective: Utilize conditional statements to guide program execution based on user input regarding weather conditions.
# File: weather_advice.py
# Directory: control-flow
# Repository: alx_be_python

def provide_weather_advice():
    """
    Asks the user for current weather conditions and provides clothing recommendations.
    Demonstrates the use of if, elif, and else statements.
    """
    # Prompt User for Weather Input
    # Use the prompt: What's the weather like today? (sunny/rainy/cold):
    weather_input = input("What's the weather like today? (sunny/rainy/cold): ").lower() # .lower() converts input to lowercase for consistent comparison

    # Provide Clothing Recommendations based on user's input
    if weather_input == "sunny":
        recommendation = "Wear a t-shirt and sunglasses."
    elif weather_input == "rainy":
        recommendation = "Don't forget your umbrella and a raincoat."
    elif weather_input == "cold":
        recommendation = "Make sure to wear a warm coat and a scarf."
    else:
        # Handles unexpected input
        recommendation = "Sorry, I don't have recommendations for this weather."

    # Output the Recommendation
    print(recommendation)

# Call the function to run the script
if __name__ == "__main__":
    provide_weather_advice()
