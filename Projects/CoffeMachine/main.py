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
currentIngredients = {
    "Water": 1000,
    "Milk": 5000,
    "Coffee": 760,
    "Money": 0.0,
}


def report():
    print(f"Water : {currentIngredients['Water']}\n")
    print(f"Milk : {currentIngredients['Milk']}\n")
    print(f"Coffee : {currentIngredients['Coffee']}\n")
    print(f"Money : {currentIngredients['Money']}\n")


def check(order):
    if currentIngredients['Water'] > MENU[order]['ingredients']['water']:
        currentIngredients['Water'] -= MENU[order]['ingredients']['water']
    else:
        print('There is not enough water')
        return False
    if currentIngredients['Coffee'] > MENU[order]['ingredients']['coffee']:
        currentIngredients['Coffee'] -= MENU[order]['ingredients']['coffee']
    else:
        print("Not enough Coffee")
        return False
    if order != 'espresso' and (currentIngredients['Milk'] > MENU[order]['ingredients']['milk']):
        currentIngredients['Milk'] -= MENU[order]['ingredients']['milk']
    elif order != 'espresso':
        print("Not enough Milk")
        return False
    return True


def change(order):
    quarters = int(input("how many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))
    total = 0
    total += 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    while total < MENU[order]['cost']:
        print("Not enough money, insert more coins")
        quarters = int(input("how many quarters?:"))
        dimes = int(input("How many dimes?:"))
        nickles = int(input("How many nickles?:"))
        pennies = int(input("How many pennies?:"))
        total += 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    currentIngredients['Money'] += MENU[order]['cost']
    print("Your change is " + str(round(total - MENU[order]['cost'],2)))


def process_order(order):
    if check(order):
        change(order)
        print('Here is your order. Enjoy!\n')


profit = 0
shouldContinue = True
while shouldContinue:
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "off":
        break
    elif order == "report":
        report()
    else:
        process_order(order)
