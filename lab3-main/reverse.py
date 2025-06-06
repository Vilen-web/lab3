def reverse_words():
    user_input = input()
    words = user_input.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

result = reverse_words()
print(result)
