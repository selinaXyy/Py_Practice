print("Welcome to the bill calculator.")

total_bill = float(input("What was the total bill amount? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100

people_to_split = int(input("How many people to split the bill? "))

#calculation
individual_bill_amount = round((total_bill * (1 + tip)) / people_to_split, 2)

print(f"Each person should pay: ${individual_bill_amount}")