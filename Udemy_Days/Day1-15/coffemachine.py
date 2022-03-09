MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

money_remain = 0


def the_choice(choice):
    print(f"Here is your {choice} ☕️. Enjoy!")
    if choice == "espresso":
        resources['water'] -= 50
        resources['coffee'] -= 18
    if choice == "latte":
        resources['water'] -= 200
        resources['milk'] -= 150
        resources['coffee'] -= 24
    if choice == "cappuccino":
        resources['water'] -= 250
        resources['milk'] -= 100
        resources['coffee'] -= 24
    return resources 


        
def coins (choice):
    money = int(input("Please insert coins.\nhow many quarters?: "))*0.25
    money += int(input("how many dimes?: "))*0.1
    money += int(input("how many nickles?: "))*0.05
    money += int(input("how many pennies?: "))*0.01
    global money_remain
    money_remain += round((money - MENU[choice]['cost']),1)
    if money >= MENU[choice]['cost']:
        print(f"Here is ${money_remain} in change.")
        the_choice(choice)           
    if money < MENU[choice]['cost']:
        print("Sorry that's not enough money. Money refunded.") 
        money_remain = 0   


def print_report():
    for key in resources:
        print(f"{key}: {resources[key]}")
    print(f"Money : ${money_remain}") 


coffe_should_continue = True 
while coffe_should_continue:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice not in ["latte", "espresso", "cappuccino", "report"]:
        coffe_should_continue = False
    if choice == "report": 
        print_report()
    if choice in ["latte", "espresso", "cappuccino"]:
        nonsuff = 0
        for item in resources:            
            if MENU[choice]['ingredients'][item] > resources[item]:
                nonsuff += 1
                print(f"Sorry there is not enough {item}.")
        if nonsuff == 0:
            coins (choice)

        



    
    

