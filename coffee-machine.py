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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#TODO 1 print all the item and quantity
user=""
profit=0

while user!="off":
    counter=0
    print("\nMenu: espresso ($1.5), latte ($2.5), cappuccino ($3.0)")
    user = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if user=="off":
        print("Shutting down... ☕ Thank you!")
        break
    elif user =="report":
        print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}ml\nMoney: ${profit:.2f}')
    elif user in MENU:
        print("Please insert coins.")
        quarters=int(input("how many quarters?: "))
        dimes=int(input("how many dimes?: "))
        nickles=int(input("how many nickles?: "))
        pennies=int(input("how many pennies?: "))
        change=(quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01)-MENU[user]["cost"]
        if change>=0:
            can_make = True
            for item in MENU[user]["ingredients"]:
                if MENU[user]["ingredients"][item] > resources[item]:
                    print(f"Sorry there isn't enough {item}.")
                    can_make = False

            if can_make:
                # Deduct ingredients
                for item in MENU[user]["ingredients"]:
                    resources[item] -= MENU[user]["ingredients"][item]
                profit += MENU[user]["cost"]
                print(f"Here is ${change:.2f} in change.\nHere is your {user} ☕️. Enjoy!")
        else:
            print("insufficient coins. Money refunded.")
    else:
        print("Invalid selection")
