from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
money_machine.report()
coffee_maker = CoffeeMaker();
coffee_maker.report()
print(coffee_maker)
print(money_machine)


