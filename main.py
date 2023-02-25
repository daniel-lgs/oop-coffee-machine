from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_on = True
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while machine_is_on:
    order = input(f"What would you like? ({menu.get_items()}): ").lower()
    if order == "off":
        break
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if menu.find_drink(order):
            menuItem = menu.find_drink(order)
            if coffee_maker.is_resource_sufficient(menuItem):
                if money_machine.make_payment(menuItem.cost):
                    coffee_maker.make_coffee(menuItem)
