scores = input("Enter 8 scores between 0 and 10 with a space separating them: ")
scores = scores.split()

for i in scores:
    scores.remove(i)
    try:
        scores.insert(0, int(i))
    except ValueError:
        exit(print("A non-integer was found in the list and the program could not be executed."))

scores.sort()
original_scores = scores[:]

highest_score = max(scores)
lowest_score = min(scores)

scores.remove(highest_score)
scores.remove(lowest_score)

average_score = sum(scores) / len(scores)

print("The original list of scores is {}.".format(original_scores))
print("The discarded scores are {} and {}, resulting in the scores list becoming {}.".format(
    lowest_score, highest_score, scores))
print("The average score is {}".format(average_score))
