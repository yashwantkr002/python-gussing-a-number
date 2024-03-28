import random

def guess_the_number():
    min_number = 1
    max_number = 100
    secret_number = random.randint(min_number, max_number)
    attempts = 0

    print("Welcome to Guess the Number Game!")
    print(f"I'm thinking of a number between {min_number} and {max_number}.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts.")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        guess_the_number()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    guess_the_number()
