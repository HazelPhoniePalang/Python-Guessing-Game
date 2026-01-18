import random

# number guessing game
low = 1
high = 100
answer = random.randint(low, high)
guesses = 0
is_running = True

print("Number guessing game")
print(f"Select a number between {low} and {high}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}")
        elif guess < answer:
            print("Your guess is too low.")
        elif guess > answer:
            print("Your guess is too high.")
        else:
            print(f"Correct! The number was {answer}.")
            print(f"You guessed it in {guesses} tries.")
            is_running = False
    else:
        print("Invalid guess.")
        print(f"Please enter a number between {low} and {high}")
