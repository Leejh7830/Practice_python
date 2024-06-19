import random
import time


def guess_number():
    number_to_guess = random.randint(1, 1000)
    guess = None
    attempts = 0
    start_time = time.time()

    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 1000: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number.")
            end_time = time.time()
            time_taken = end_time - start_time
            print(f"You took {attempts} attempts and {time_taken:.2f} seconds to guess the number.")


if __name__ == "__main__":
    guess_number()