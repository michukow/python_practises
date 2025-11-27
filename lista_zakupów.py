def preparing_shopping_list():
    shopping_list = {}

    while True:
        name = input("Insert name of product: ")
        if name.lower() == "stop":
            break
        if not name:
            print("Wrong product name. Try again!")
            continue
        category = input(f"Insert a category of {name}: ")
        if not category:
            print("Wrong category. Try again!")
            continue
        try:
            price = float(input(f"Insert a price of {name}: "))
            if price <= 0:
                print("Price must be positive!")
                continue
        except ValueError:
            print("Error: price must be a number.")
            continue
        if category not in shopping_list:
            shopping_list[category] = []
        shopping_list[category].append(price)

    print("Your shopping list:")
    print(shopping_list)

preparing_shopping_list()

def statistics(shopping_list):
	for kategoria in category:
		for cena in price:
            suma+=cena

			