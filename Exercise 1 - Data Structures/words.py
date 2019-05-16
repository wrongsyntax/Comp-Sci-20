words = ['Roses', 'are', 'red', 'Violets', 'are', 'blue',
         'Computer', 'Science', 'is', 'fun', 'Python', 'is', 'too']

number = int(input("Enter a number: "))


def find_words(num, word_list):
    found = []
    for word in word_list:
        if len(word) >= num:
            found.append(word)
        else:
            pass

    return found


new_words = find_words(number, words)

print("The words that are longer than {} are {}.".format(number, new_words))
