word = input("Enter a word: ")


def count_vowels(word):
    vowel_count = 0
    word = list(word)
    for i in range(len(word)):
        if "a" in word[i]:
            vowel_count += 1
        elif "e" in word[i]:
            vowel_count += 1
        elif "i" in word[i]:
            vowel_count += 1
        elif "o" in word[i]:
            vowel_count += 1
        elif "u" in word[i]:
            vowel_count += 1

    return vowel_count


vowels = count_vowels(word)
print("The word \"{}\" has {} vowels.".format(word, vowels))
