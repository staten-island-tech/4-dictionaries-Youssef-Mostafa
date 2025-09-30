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
    "description": "High efficiency washing machine win 10 wash cycles and quiet washing."
}

,{
    "name": "Mecity 4-Slice Touchscreen Toaster, Stainless Steel",
    "price": 79.99,
    "department": "Cooking",
    "description": "Has 6 different toasting settings with a fully function touchscreen display and easy cleaning."
}

,{
    "name": "COWIN Bluetooth Headphones Active Noise Cancelling Headphones Wireless Headphones",
    "price": 21.99,
    "department": "Devices",
    "description": "Bluetooth headphones with comfortable ear cushions and active noise cancelling."
}

,{
    "name": "SteelSeries Apex 3 TKL RGB Gaming Keyboard ",
    "price": 34.99,
    "department": "Gaming",
    "description": "Compact, water and dust resistant RGB keyboard with durable switches."
}

,{
    "name": "Suevery Gaming PC, AMD Ryzen 5 5600GT, Vega 7 Graphics, 16GB DDR4 RAM, 512GB SSD, Wi-Fi 6-White",
    "price": 465.99,
    "department": "Gaming",
    "description": "Fast 5600Gt processor for, Vega 7 graphics, and tons of storage and ram for an immersive and smooth gameplay experience."
}

,{
    "name": "LOLYKITCH Tri-Ply Stainless Steel Pan Set, 8.5-Inch, 10-Inch, 12-Inch Chef & Frying Pan",
    "price": 59.99,
    "department": "Cooking",
    "description": "A set of 3 frying pans that are induction and oven safe. Durable and long lasting."
}

,{
    "name": "Yelomin Magnetic Portable Charger, 10000mAh Magsafe Power Bank",
    "price": 22.99,
    "department": "Devices",
    "description": "A portable charger with strong magsafe and a build in USB-C charger and other chargers for all phones."
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
    purchase = input("What item number would do you want to purchase? Or would you like to view cart and checkout?")
    purchase = int(purchase)
    if purchase == len(Walmart) + 1:
        print(cart)
    elif purchase == len(Walmart) +2:
        print(f"Items: {cart}. Total: {total}")
        checkout = input("Do you want to check out?")
        if checkout == "yes" or checkout == "y":
            print("Your purchase has been confirmed. Thank you for shopping.")
            quit()
        elif checkout == "no" or checkout == "n":
            print("Your purchase has been cancelled. Please come again.")
            quit()
    
    else:
        purchase = int(purchase)
        purchase = purchase - 1
        confirmation = input(f"You have chose {Walmart[purchase]["name"]}. Are you sure you would like to purchase this?")
        if confirmation == "yes" or confirmation == "y":
            print("Your item has been added to cart. You may continue browsing or checkout.")
            cart.append(Walmart[purchase]["name"])
            total = total + Walmart[purchase]['price']
        elif confirmation == "no" or confirmation == "n":
            print("Your ietm was not added to cart. You may continue browsing or checkout.")
        else:
            print("That is not a valid input. Try again.")

            