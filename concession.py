menu = {"popcorn":1.00,
        "hot dog":2.00,
        "giant pretzel":2.00,
        "soda":1.00}

cart=[]
total=0

for key, value in menu.items():
    print(f"{key:15}: ${value:.2f}")

while True:
    food= input("Select an item (q to quit): ").lower()
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total+=menu.get(food)


print("your total is ", total)


    
