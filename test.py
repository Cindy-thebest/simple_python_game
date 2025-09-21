import random

print("Welcome to the Number Guessing Game! ")
# Computer picks a random number between 1 and 20
secret_number = random.randint(1, 20)
attempts = 0
guess = 0

print("I have picked a number between 1 and 40. Can you guess it?")
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f" Congratulations! You guessed it in {attempts} tries.")
print("Thanks for playing!")