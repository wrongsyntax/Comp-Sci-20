def check(number, number_range):
    if number in range(number_range + 1):
        return True
    else:
        return False


number = int(input("Enter the number you want to check for: "))
num_range = int(input("Enter the range to check for the number (ex. 10): "))
checked = check(number, num_range)
if checked:
    print("The number {} is in the range of {}".format(number, num_range))
else:
    print("The number {} is not in the range of {}".format(number, num_range))
