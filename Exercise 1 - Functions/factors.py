def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


number = int(input("Enter a number: "))
factors = str(find_factors(number))
factors = factors.replace("[", "")
factors = factors.replace("]", "")
print("The factors of {} are {}".format(str(number), factors))
