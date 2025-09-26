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

<<<<<<< HEAD
for index, item in enumerate(Walmart, start = 1):
    print(index, ":", item)
=======

for index, item in enumerate(Walmart[1:], start = 1):
    print(index, ":", item["name"])
>>>>>>> 7e4f9b349311a94e7e15f7d10ae20486e112c6da
purchase = input("What item number would do you want to purchase?")
purchase = int(purchase)
purchase = purchase - 1
confirmation = input(f"You have chose {Walmart[purchase]["name"]}. Are you sure you would like to purchase this?")

if confirmation == "yes" or confirmation == "y":
    print("Your purchase was successful. Thank you.")
elif confirmation == "no" or confirmation == "n":
    print("Your purchase has been cancelled. Come again next time.")
else:
<<<<<<< HEAD
    print("That is not a valid input. Try again.") """
=======
    print("That is not a valid option.")
>>>>>>> 7e4f9b349311a94e7e15f7d10ae20486e112c6da


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
cart = ["Cart printed"]
while checkout is not "Done":
    for index, item in enumerate(Walmart, start = 1):
        print(index, ":", item)
    print(f"{len(Walmart) + 1 } : View Cart")
    purchase = input("What item number would do you want to purchase? Or would you like to view cart?")
    if purchase == len(Walmart) + 1:
        print(cart)
    elif purchase.isdigit:
        purchase = int(purchase)
        purchase = purchase - 1
        confirmation = input(f"You have chose {Walmart[purchase]["name"]}. Are you sure you would like to purchase this?")
        if confirmation == "yes" or confirmation == "y":
            print("Your item has been added to cart. You may continue browsing.")
            cart.append(purchase)
        elif confirmation == "no" or confirmation == "n":
            print("Your ietm was not added to cart. You may continue browsing.")
        else:
            print("That is not a valid input. Try again.")