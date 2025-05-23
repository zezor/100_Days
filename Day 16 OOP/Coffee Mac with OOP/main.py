from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
print(menu.get_items())

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


is_on = True

while is_on :
    options =menu.get_items()
    choice = input(f"What will you like to take {options} ?")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)

        # if coffee_maker.is_resource_sufficient(drink):
        #     if money_machine.make_payment(drink.cost):
        #         coffee_maker.make_coffee(drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)