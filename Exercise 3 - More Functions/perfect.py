num = int(input("Enter a number to check if it is perfect: "))


def test_perfect(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number


test = test_perfect(num)

if test:
    print("{} is a perfect number.".format(num))
else:
    print("{} is not a perfect number.".format(num))
