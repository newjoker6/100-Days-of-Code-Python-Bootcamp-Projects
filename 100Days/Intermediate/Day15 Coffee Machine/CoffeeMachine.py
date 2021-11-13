import sys

MachineData = {
    'Water': 300,
    'Milk': 200,
    'Coffee': 100,
    'Money': 0
}

DrinkPrices = {
    'espresso': 1.50,
    'latte': 2.50,
    'cappuccino': 3.00
}

DrinkRecipes = {
    'espresso': {
        'Water': 50,
        'Coffee': 18
    },
    'latte': {
        'Water': 200,
        'Coffee': 24,
        'Milk': 150
    },
    'cappuccino': {
        'Water': 250,
        'Coffee': 24,
        'Milk': 100
    }
}



def check_stock():
    for ingredient in DrinkRecipes[UserCommand]:
        if DrinkRecipes[UserCommand][ingredient] > MachineData[ingredient]:
            print("Not enough ingredients available")
            break

def make_drink():
    for ingredient in DrinkRecipes[UserCommand]:
        MachineData[ingredient] -= DrinkRecipes[UserCommand][ingredient]

def get_money():
    pennies_amount = int(input("How many pennies?: "))
    nickles_amount = int(input("How many nickles?: "))
    dimes_amount = int(input("How many dimes?: "))
    quarters_amount = int(input("How many quarters?: "))

    total = calculate_money_given(pennies_amount, nickles_amount, dimes_amount, quarters_amount)

    return total

def calculate_money_given(pennies_amount, nickles_amount, dimes_amount, quarters_amount):
    Total = (0.01 * pennies_amount) + (0.05 * nickles_amount) + (0.10 * dimes_amount) + (0.25 * quarters_amount)
    return Total

def calculate_change(money, price):
    change_amount = money - price
    return change_amount

def process_drink(given, drink):
    if given < DrinkPrices[drink]:
        print("Insufficient funds, refund in progress")
    elif given == DrinkPrices[drink]:
        make_drink()
    elif given > DrinkPrices[drink]:
        make_drink()
        change = calculate_change(given, DrinkPrices[drink])
        print(f"Here is your change ${change}")

Drinks = DrinkRecipes.keys()
Machine_Running = True

while Machine_Running:
    UserCommand = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if UserCommand == "report":
        print(f"Water: {MachineData['Water']}ml"f"\nMilk: {MachineData['Milk']}ml"f"\nCoffee: {MachineData['Coffee']}g" f"\nMoney: ${MachineData['Money']}")

    elif UserCommand in Drinks:
        check_stock()
        TotalMoneyGiven = get_money()
        process_drink(TotalMoneyGiven, UserCommand)
        MachineData['Money'] += DrinkPrices[UserCommand]

    elif UserCommand == 'shutdown':
        sys.exit(0)

    else:
        print("Drink not accepted")

