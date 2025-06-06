import random

def guess_the_number():
    print("Hello! What is your name?")
    player_name = input()

    secret_number = random.randint(1, 20)
    print(f"Well,{player_name}, I am thinking of a number between 1 and 20.")

    c = 0
    while True:
        print("Take a guess.")
        guess = int(input())

        c += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {player_name}! You guessed my number in {c} guesses!")
            break

guess_the_number()
