
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}

def is_source_sufficient(order_ingredient):
    is_enough=True
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"There is not enough {item}")
            is_enough=False
    return is_enough

def process_coin():
    total= int(input("how many quaters"))* 0.25
    total += int(input("how many dimes"))* 0.1
    total += int(input("how many nickles"))* 0.05
    total += int(input("how many pennies"))* 0.01
    return total

def transaction_succesful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change= round(money_recieved - drink_cost, 2)
        global profit
        profit += drink_cost
        print(f"here is money {drink_cost}")
        return True
    else:
        print("You have not inserted enough money")
        return False

def make_coffee(drink_name,order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"here is your {drink_name}☕ ")




is_on=True
while is_on:
    choice=input("What would you like (cappuccino/latte/espresso): ")
    if choice == "off":
        is_on = False
    elif choice== "report":
        print(resources)
        print(f"water:{resources['water']}ml")
        print(f"milk::{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}ml")
        print(f"money:{profit}$")
    else:
        drink=MENU[choice]
        if is_source_sufficient(drink["ingredients"]):
            payments= process_coin()
            if transaction_succesful(payments,drink["cost"]):
                make_coffee(choice,drink["ingredients"])


