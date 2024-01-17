import os # it is used to clear screen
def add(a,b):
    return a + b
def subtract(a,b):
    return a + b
def multiply (a,b):
    return a * b
def divide (a,b):
    return a/b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    number_1 = float(input("enter the first number:\n"))
    for i in operations:
        print(i)
    continue_flag = True
    while continue_flag:
        symbol_to_use = input("pick an operation: ") # +, -, *...
        number_2 = float(input("enter second number: \n"))
        calculator_function = operations[symbol_to_use] #add, subtract, ..
        output = calculator_function(number_1,number_2) #calculator_function is a variable not a function in real sence
        print(f"{number_1} {symbol_to_use} {number_2} = {output}")

        should_continue = input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit: ").lower()
        if should_continue == 'y':
            number_1 = output
        elif should_continue == 'n':
            continue_flag = False
            os.system('cls')
            calculator()  #recursion
        else:
            continue_flag = False
            print("See yeah")
calculator()


