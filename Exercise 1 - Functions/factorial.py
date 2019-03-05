def factorial(number):
    product = 1
    for i in range(number):
        product = product * (i + 1)
    return product


number = int(input("What number would you like the factorial of? "))
print("The factorial of " + str(number) + " is " + str(factorial(number)))
