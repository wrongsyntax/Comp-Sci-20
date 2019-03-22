num = int(input("Enter a number to check if it's prime: "))


def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


test = is_prime(num)

if test:
    print("The number {} is prime.".format(num))
else:
    print("The number {} is not prime.".format(num))
