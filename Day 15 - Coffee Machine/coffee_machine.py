

MENU = {
    "espresso": {
        "ingredient": {
            "water": 50,
            "milk" : 0,
            "coffee": 18
        },
        "cost": 1.5
    },

    "latte": {
        "ingredient": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5},

    "cappucino": {
        "ingredient": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def MAIN(resources):
    breaker = ""
    while True:
        if breaker == "break":
            break
        while True:
            responce = input("What drink would you like (Latte,Cappucino,Espresso)? ")
            responce = responce.lower()
            if (responce != "latte" and responce != "cuppucino" and responce != "espresso" and responce != "report"):
                if responce == "off":
                    breaker = "break"
                    break
                elif responce == "fill":
                    resources["water"] = 300
                    resources["milk"] = 200
                    resources["coffee"] = 100
                    break
                else:
                    print("Im sorry, I don't understand.")
                    break

            if responce != "report":
                choice = MENU[responce]
                if resources["water"] < choice["ingredient"]["water"] or resources["milk"] < choice["ingredient"]["milk"] or resources["coffee"] < choice["ingredient"]["coffee"]:
                    print("Insufficient resources")
                    break
            else:
                print(  "Water : ", resources["water"], "\n",
                        "Milk : ", resources["milk"], "\n",
                        "Coffee : ", resources["coffee"], "\n",
                        "Money : ", resources["money"], "\n")
                break
                
                    
            print("Insert coin, Cost is £" + str(choice["cost"]))
            one = int(input("number of 1ps: "))
            two = int(input("number of 2ps: "))*2
            five = int(input("number of 5ps: "))*5
            ten = int(input("number of 10ps: "))*10
            twenty = int(input("number of 20ps: "))*20
            fifty = int(input("number of 50ps: "))*50
            pound = int(input("number of £1s: "))*100
            twopound = int(input("number of £2s: "))*200
            total = float((one+two+five+ten+twenty+fifty+pound+twopound)/100)


            if total < choice["cost"]:
                print("Insufficient monies given. Please return to selction")
                break
            
            change = total - choice["cost"]
            resources["water"] -= choice["ingredient"]["water"]
            resources["milk"] -= choice["ingredient"]["milk"]
            resources["coffee"] -= choice["ingredient"]["coffee"]
            resources["money"] += choice["cost"]
            print(responce, "Dispenced, £" + str(round(change,2)),"change given. Enjoy your coffee! :)")

MAIN(resources)


            
