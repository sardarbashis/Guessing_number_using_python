# for getting random something
import random

def guess(x):
    guess = 0
    # for -> random.randint(a, b)
    # Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
    random_guess = random.randint(1,x)
    while guess != random_guess :
        guess  = int(input(f"Enter a Nuber between 1 and {x}:"))
        if guess < random_guess:
            print(f"Sorry, guess again. Too low.")
        elif guess > random_guess:
            print(f"Sorry, guess agin. Too high.")

    print(f"Yay, Congrats. You have guessed the number {random_guess} correctly.")

guess(10)