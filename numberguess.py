import random

def number_guessing_game():
    print(" Welcome to Number Guessing Game!")
    print("I will choose a number between 1 and 100.")

    # Generate random number
    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 10   # optional limit

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            # Hint system
            if guess < secret_number:
                print(" Too low!")
            elif guess > secret_number:
                print(" Too high!")
            else:
                print(f" Correct! You guessed it in {attempts} attempts.")
                break

            # Optional attempt limit
            if attempts >= max_attempts:
                print(f" Game Over! The number was {secret_number}")
                break

        except ValueError:
            print(" Invalid input! Please enter a number.")

# Run the game
number_guessing_game()