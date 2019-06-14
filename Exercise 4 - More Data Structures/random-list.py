from random import randint

original_list = []
above_avg = []
below_avg = []

for i in range(10):
    original_list.append(randint(0, 99))

original_list.sort()

average = sum(original_list) / len(original_list)

for i in original_list:
    if i > average:
        above_avg.append(i)
    elif i < average:
        below_avg.append(i)
    else:
        pass

print("""

------------------------------------------------
                    SUMMARY
------------------------------------------------

ORIGINAL LIST .......... {}

AVERAGE ................ {}

NUMBERS ABOVE AVERAGE .. {}

NUMBERS BELOW AVERAGE .. {}

""".format(original_list, average, above_avg, below_avg))
