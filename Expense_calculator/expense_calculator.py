print("===================================")
print("      EXPENSE CALCULATOR")
print("===================================")

user_name = input("Enter your name: ")

monthly_budget = float(input("Enter your monthly budget (₹): "))

expense_count = int(input("How many expenses do you want to add? "))

spent_money = 0

print("\nEnter your expenses:")

for count in range(expense_count):
    amount = float(input(f"Expense {count + 1}: ₹"))
    spent_money += amount

balance = monthly_budget - spent_money

print("\n========== REPORT ==========")
print("Name           :", user_name)
print("Budget         : ₹", monthly_budget)
print("Total Spent    : ₹", spent_money)

if balance > 0:
    print("Money Saved    : ₹", balance)
    print("Status         : Great! You are within your budget.")

elif balance == 0:
    print("Money Saved    : ₹0")
    print("Status         : You used your complete budget.")

else:
    print("Overspent By   : ₹", abs(balance))
    print("Status         : Warning! You exceeded your budget.")

print("============================")
print("Thank you for using the Expense Calculator!")