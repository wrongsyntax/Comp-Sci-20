num = int(input("Enter a number to check if it's prime: "))


def test_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


tested = test_prime(num)

if tested:
    print("The number {} is prime.".format(num))
else:
    print("The number {} is not prime.".format(num))