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
    "money": 0
}


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def take_order():
    order = input("What would you like? (espresso/latte/cappuccino)").lower()
    return order


# TODO: 3. Print report of all coffee machine resources.
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${resources['money'] }")


# TODO: 4. Check resources are sufficient to make drink order.
def check_resources(order):
    order_water_qty = MENU[order]['ingredients']['water']
    order_milk_qty = MENU[order]['ingredients']['milk']
    order_coffee_qty = MENU[order]['ingredients']['coffee']
    if resources['water'] < order_water_qty:
        print("Sorry there is not enough water.")
        return False
    elif resources['milk'] < order_milk_qty:
        print("Sorry there is not enough milk.")
        return False
    elif resources['coffee'] < order_coffee_qty:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


# TODO: 5. Process coins.
def process_coins(quarters, dimes, nickles, pennies):
    total_quarters = quarters * 0.25
    total_dimes = dimes * 0.10
    total_nickles = nickles * 0.05
    total_pennies = pennies * 0.01
    amount_paid = total_quarters + total_dimes + total_nickles + total_pennies
    return amount_paid


# TODO: 6. Check transaction successful?
def check_transaction(amount_paid, order):
    order_cost = MENU[order]['cost']
    if amount_paid < order_cost:
        print("Sorry that's not enough money. Money refunded.”")
        return False
    elif amount_paid > order_cost:
        change = round(amount_paid - order_cost, 2)
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        resources["money"] += order_cost
        return True


# TODO: 7. Make Coffee.
def make_coffee(order):
    resources['water'] -= MENU[order]['ingredients']['water']
    resources['milk'] -= MENU[order]['ingredients']['milk']
    resources['coffee'] -= MENU[order]['ingredients']['coffee']
    print(f"Here is your {order}. Enjoy ☕️!”")


# Main function for Coffee MakingMachine
def coffee_machine():
    shop_is_open = True

    while shop_is_open:
        order = take_order()

        # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
        if order == 'off':
            shop_is_open = False
            return
        elif order == 'report':
            print_report()
        else:
            sufficient_resources = check_resources(order)

            if not sufficient_resources:
                shop_is_open = True
            else:
                print("Please insert coins.")
                quarter_qty = int(input("how many quarters?: "))
                dimes_qty = int(input("how many dimes?: "))
                nickles_qty = int(input("how many nickles?: "))
                pennies_qty = int(input("how many pennies?: "))
                amount_paid = process_coins(quarter_qty, dimes_qty, nickles_qty, pennies_qty)
                transaction_successful = check_transaction(amount_paid, order)
                if not  transaction_successful:
                    shop_is_open = True
                else:
                    make_coffee(order)


coffee_machine()



