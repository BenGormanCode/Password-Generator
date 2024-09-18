import typer
import inquirer  # noqa
from generator import Generator

# Welcome to the Password Generator App

# How long would you like your password to be?


def password_length():
    while True:
        try:
            user_input = int(
                input("How long would you like your password to be?: "))
            if 7 < user_input < 21:
                print(f"Your password will be {user_input} characters")
                break
            else:
                print("The length must be between 8-20 characters.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return user_input
# Specify Character Types (Checkbox from inquirer)


def main():
    categories = [
        inquirer.Checkbox(
            "categories",
            message="What would you like included in your password?",
            choices=["Upper Case", "Lower Case", "Numbers",
                     "Symbols"],
            default=["Upper Case", "Lower Case"],
        ),
    ]
    length = password_length()
    answers = inquirer.prompt(categories)
    password = Generator(length, answers.get("categories"))
    print(password.generate())


if __name__ == "__main__":
    typer.run(main)

# Output generated password


# Would you like to re-generate?
