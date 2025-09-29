""" You will be creating a little store in your terminal. You will have a list of
dictionaries that will be displayed to the user. Each Dictionary will have at
least 3 properties (name, price and whatever you want)
PART ONE:
The user will select one item to purchase. You will then show the user
ONLY the name of the item they purchased. You will need to use the item
index to accomplish this task.

PART TWO:
You will now make the app more complex by incorporating while loops and
a “cart”. Users will be shown the list of items and asked to purchase one.
Afterwards ask the user if they wish to continue. Once the user has decided
they are done shopping, print the names of the items purchased and the
total of the cart. """


# part one of dictionary project

""" cleanly_bundle = {
    "name": "Method Men Sea Surf Body Wash & Glacier + Granite Shampoo",
    "price": 14.39,
    "department": "Hygiene",
    "description": "A special bundle of cool glacier shampoo and crisp, salty body wash by Method Men"
}

tv = {
    "name": "LG 86 4K UHD UA75 AI Smart TV",
    "price": 798.00,
    "department": "Entertainment",
    "description": "Really smooth and high quality video enhanced with AI and a smart TV microchip"
}


vacuum = {
    "name": "Dyson V11 Extra Cordless Vacuum Cleaner",
    "price": 449.99,
    "department": "Housekeeping",
    "description": "Lightweight, cordless vacuum that has no touch bin emptying and wall mounting and charging"
}

washing_machine = {
    "name": "28 Wide 4.8 Cu Ft. Front Loading Washing Machines Washer - White",
    "price": 779.00,
    "department": "Washing",
    "description": "High efficeincy washing machine win 10 wash cycles and quite washing."
}


Walmart = [None, cleanly_bundle, tv, vacuum, washing_machine]


for index, item in enumerate(Walmart, start = 1):
    print(index, ":", item)


for index, item in enumerate(Walmart[1:], start = 1):
    print(index, ":", item["name"]
purchase = input("What item number would do you want to purchase?")
purchase = int(purchase)
purchase = purchase - 1
confirmation = input(f"You have chose {Walmart[purchase]["name"]}. Are you sure you would like to purchase this?")

if confirmation == "yes" or confirmation == "y":
    print("Your purchase was successful. Thank you.")
elif confirmation == "no" or confirmation == "n":
    print("Your purchase has been cancelled. Come again next time.")
else:
    print("That is not a valid input. Try again.") """



# part two of dictionary project

Walmart = [{
    "name": "Method Men Sea Surf Body Wash & Glacier + Granite Shampoo",
    "price": 14.39,
    "department": "Hygiene",
    "description": "A special bundle of cool glacier shampoo and crisp, salty body wash by Method Men"
}

,{
    "name": "LG 86 4K UHD UA75 AI Smart TV",
    "price": 798.00,
    "department": "Entertainment",
    "description": "Really smooth and high quality video enhanced with AI and a smart TV microchip"
}


,{
    "name": "Dyson V11 Extra Cordless Vacuum Cleaner",
    "price": 449.99,
    "department": "Housekeeping",
    "description": "Lightweight, cordless vacuum that has no touch bin emptying and wall mounting and charging"
}

,{
    "name": "28 Wide 4.8 Cu Ft. Front Loading Washing Machines Washer - White",
    "price": 779.00,
    "department": "Washing",
    "description": "High efficeincy washing machine win 10 wash cycles and quite washing."
}]


checkout = "Not finished."
confirmation = "Not done choosing."
total = 0
cart = []
while checkout is not "y" or not "yes":
    for index, item in enumerate(Walmart, start = 1):
        print(index, ":", item)
    print(f"{len(Walmart) + 1 } : View Cart")
    print(f"{len(Walmart) + 2 } : Checkout")
    purchase = input("What item number would do you want to purchase? Or would you like to view cart?")
    purchase = int(purchase)
    if purchase == len(Walmart) + 1:
        print(cart)
    elif purchase == len(Walmart) +2:
        print(f"Items: {cart}. Total: {total}")
        checkout = input("Do you want to check out?")
        if checkout == "no" or checkout == "n":
            print("Your purchase has been cancelled.")
            quit()

    else:
        purchase = int(purchase)
        purchase = purchase - 1
        confirmation = input(f"You have chose {Walmart[purchase]["name"]}. Are you sure you would like to purchase this?")
        if confirmation == "yes" or confirmation == "y":
            print("Your item has been added to cart. You may continue browsing.")
            cart.append(Walmart[purchase]["name"])
            print(cart)
            total = total + Walmart[purchase]['price']
        elif confirmation == "no" or confirmation == "n":
            print("Your ietm was not added to cart. You may continue browsing.")
        else:
            print("That is not a valid input. Try again.")

            