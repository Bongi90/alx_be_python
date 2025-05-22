# User Input for Financial Details
# It's crucial to convert input to a float since income/expenses can be decimals
monthly_income_str = input("Enter your monthly income: ")
monthly_income = float(monthly_income_str) # Convert to float for decimal values

monthly_expenses_str = input("Enter your total monthly expenses: ")
monthly_expenses = float(monthly_expenses_str) # Convert to float

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings with simple interest
# Assume a simple annual interest rate of 5% (0.05 as a decimal)
annual_interest_rate = 0.05

# Simplified formula: Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
# This is equivalent to: Projected Savings = (Monthly Savings * 12) * (1 + 0.05)
annual_savings_without_interest = monthly_savings * 12
interest_earned = annual_savings_without_interest * annual_interest_rate
projected_annual_savings = annual_savings_without_interest + interest_earned


# Output Results
print(f"Your monthly savings are ${monthly_savings:.2f}.") # .2f for 2 decimal places
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")