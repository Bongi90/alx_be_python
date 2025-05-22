# Prompt the user for their current age
# The input() function reads a string, so we convert it to an integer using int()
current_age_str = input("How old are you? ")
current_age = int(current_age_str)

# Calculate how old the user will be in 2050
# Assuming current year is 2023, 2050 is 27 years from now.
years_to_add = 27
future_age = current_age + years_to_add

# Print the user's age in 2050
print(f"In 2050, you will be {future_age} years old.")