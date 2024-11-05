from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

c = CoffeeMaker()
mm = MoneyMachine()
m = Menu()
breaker = True

while breaker:
    while breaker:
        drinks = m.get_items()
        responce = input("Hello, which coffee would you like? " + str(drinks)[:-1] + ": ").lower()
        if responce == "off":
            breaker = False
            break
        elif responce == "report":
            c.report()
            mm.report()
            break
        while m.find_drink(responce) == "" or c.is_resource_sufficient(m.find_drink(responce)) != True:
            responce = input("Hello, which coffee would you like? " + str(drinks)[:-1] + ": ")

        while mm.make_payment(m.find_drink(responce).cost) == False:
            wait = True  
        c.make_coffee(m.find_drink(responce))
        break
