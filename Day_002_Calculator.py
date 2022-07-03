# Datatypes, Numbers, Operations, Type conversion, f-strings
print("Welcome to the tip calculator")
total = float(input("\n What was the total bill?"))
percentage = float(input("\n What percentage tip would you like to give? 10, 12, or 15?"))
total += total * (percentage / 100)
numbers = input("\n How many people should split the bill?")
total /=float(numbers)
print(f"\nEach person should pay: {round(total,2)}")
