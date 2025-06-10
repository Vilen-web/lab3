def grams_to_ounces(grams):
    return 28.3495231 * grams


def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)


def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return "No solution"



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(nums):
    return list(filter(is_prime, nums))


import itertools

def string_permutations():
    s = input("Enter a string: ")
    perms = itertools.permutations(s)
    for perm in perms:
        print(''.join(perm))


def reverse_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    return ' '.join(reversed(words))


def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


def spy_game(nums):
    return '0' in nums and '0' in nums[nums.index(0)+1:] and '7' in nums[nums.index(0)+1:]


import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3


def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst


def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


def histogram(lst):
    for num in lst:
        print('*' * num)




import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guess_count = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guess_count += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guess_count} guesses!")
            break


