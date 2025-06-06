def is_palindrome(s):
    return s == s[::-1]

word = input()
result = is_palindrome(word)
print(result) 
