import calculator
import guess_number
import utils


def main():
    utils.print_welcome_message()

    while True:
        print("\nChoose an option:")
        print("1. Use Calculator")
        print("2. Play Guess the Number")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            calculator.calculator()
        elif choice == '2':
            guess_number.guess_number()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
        main()