type_pizza = input("what size of pizza do you want S/M/L:")
pizza_cost = 0
if type_pizza == "S" or type_pizza == "s":
    pizza_cost = 100
    pepper_only = input("Do you want pepper only (y/n): ")
    if pepper_only == "y" or pepper_only == "Y":
        pizza_cost = (pizza_cost + 30)
        print(pizza_cost)

elif type_pizza == "M" or type_pizza == "s":
    pizza_cost = 200
    pepper_only = input("Do you want pepper only (y/n): ")
    if pepper_only == "y" or pepper_only == "Y":
        pizza_cost = (pizza_cost + 50)
        print(pizza_cost)
else:
    pizza_cost = 300
    print(f"Your pizza cost is {pizza_cost}")


extra = input("Do you want extra cheese (y/n): ")
if extra == "y" or extra == "Y":
    pizza_cost = pizza_cost + 50
print(f"Your total cost is {pizza_cost}")


