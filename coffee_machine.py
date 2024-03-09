MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

ONE_QUARTER = 0.25
ONE_DIME = 0.10
ONE_NICKLE = 0.05
ONE_PENNY = 0.01

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#functions
def check_resources(coffee_type):
    coffee_avaliable = True
    for ingredient in MENU[coffee_type]["ingredients"]: #keys (e.g. "water")
            #values                             #values
        if resources[ingredient] - MENU[coffee_type]["ingredients"][ingredient] < 0:
            print(f"Sorry, there is not enough {ingredient}.")
            coffee_avaliable = False

    return coffee_avaliable

def process_coins():
    print("Please enter the amount of money you are paying.")
    quarters_amount = float(input("How many quarters? ")) * ONE_QUARTER
    dimes_amount = float(input("How many dimes? ")) * ONE_DIME
    nickles_amount = float(input("How many nickles? ")) * ONE_NICKLE
    pennies_amount = float(input("How many pennies? ")) * ONE_PENNY

    return quarters_amount + dimes_amount + nickles_amount + pennies_amount

def check_user_payment(drink_cost, user_payment):
    if user_payment == drink_cost:
        print("Payment successful!")
        return True
    elif user_payment > drink_cost:
        change = user_payment - drink_cost
        print(f"Payment successful! Here is ${round(change, 2)} dollars in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def deduct_resources(coffee_type, resources):
                        #keys
    for ingredient in MENU[coffee_type]["ingredients"]:
            #values                     #values
        resources[ingredient] -= MENU[coffee_type]["ingredients"][ingredient]

def print_report(profit):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${round(profit, 2)}")

#final program
def coffee_machine():
    #declarations
    profit = 0.0
    machine_on = True
    user_response = ""
    coffee_type = ""

    while machine_on:
        print("espresso $1.5\nlatte $2.5\ncappuccino $3.0")
        user_response = input("What would you like?: ").strip().lower()
        if user_response == "espresso" or user_response == "latte" or user_response == "cappuccino":
            coffee_type = user_response
            coffee_avaliable = check_resources(coffee_type)
            if coffee_avaliable:
                user_payment = process_coins()
                payment_successful = check_user_payment(MENU[coffee_type]["cost"], user_payment)
                if payment_successful:
                    deduct_resources(coffee_type, resources)
                    profit += MENU[coffee_type]["cost"]
                    print(f"Here is your {coffee_type} ☕. Enjoy!")
        elif user_response == "report":
            print_report(profit)
        elif user_response == "off":
            machine_on = False
        else:
            print("Invalid input. Try again.")

        print("\n")

coffee_machine()