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
balance = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def calculate_inserted_coins():
    quarters = float(input("How many quarters?"))
    dimes = float(input("How many dimes?"))
    nickles = float(input("How many nickles?"))
    pennies = float(input("How many pennies?"))

    total = round(float(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01),2)
    print(f"Total money inserted: {total}")
    return total

def create_report(resources):
    for key, value in resources.items():
        #print(f"{key.capitalize()}: {value}")
        if key in ['water', 'milk']:
            print(f"{key.capitalize()}: {value}ml")
        elif key in ['coffee']:
            print(f"{key.capitalize()}: {value}mg")
    global balance
    print(f"Money: ${balance}")

def check_resources(user_input):
    if user_input in MENU:
        ingredients = MENU[user_input]["ingredients"]
        for item in ingredients:
            if resources.get(item, 0) < ingredients[item]:
                print(f"Sorry, not enough {item}.")
                return False
        print(f"Enough resources to make {user_input}!")
        return True
    else:
        print(f"Drink type {user_input} doesn't exist!")
        return False

def process_coins(user_input):
    total = calculate_inserted_coins()

    cost = MENU[user_input]["cost"]
    if cost > total:
        print(f"Sorry that's not enough money. Money refunded.")
        return False
    elif total > cost:
        balance = round(total - cost,2)
        print(f"Inserted amount: {total}, drink cost {cost}, remaining balance {balance}")
        return True
    print(f"Enough resources to make {user_input}!")
    return True


def make_coffee(user_input, resources):
    ingredients = MENU[user_input]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {user_input}. Enjoy!")


def coffee_machine():

    balance = 0

    is_machine_on = True
    while is_machine_on:
        user_input = input("What would you like? (espresso/latte/cappuccino):").lower()

        if user_input == 'off':
            is_machine_on = False
            print("Shutting down ...")
        elif user_input == 'report':
            create_report(resources)
        elif user_input in MENU:
            if check_resources(user_input):
                if process_coins(user_input):
                    make_coffee(user_input, resources)
                    balance += MENU[user_input]["cost"]

        else:
            print("Invalid input.")



coffee_machine()