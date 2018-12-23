# Write a Python program to find the list of words that are longer than n from a given list of words.


def long_words(num, str):
    word_length = []
    txt = str.split(" ")
    for i in txt:
        if len(i) > num:
            word_length.append(i)
    return word_length


print(long_words(3, "Write a Python program to find the list of words that are longer"
                    " than n from a given list of words. "))
