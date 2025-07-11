monthly_income_string = input("Enter your monthly income:")

monthly_expenses_string = input("Enter your total monthly expenses:")

monthly_income = int(monthly_income_string)

monthly_expenses = int(monthly_expenses_string)

monthly_savings = monthly_income - monthly_expenses

projected_savings = monthly_savings *12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")