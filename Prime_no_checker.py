def prime_checker(number):
    is_prime =True
    if number ==1:
        is_prime = False
    for i in range(2, number):
        if number%i ==0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("Not a prime number")

n= int(input("enter a number:"))
prime_checker(n)

# second method

import math
def prime_checker(number):
    is_prime =True
    if number ==1:
        is_prime = False
    for i in range(2, math.ceil(number/2)+ 1):
        if number%i ==0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("Not a prime number")

n= int(input("enter a number:"))
prime_checker(n)