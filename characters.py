import string


def lowercase_alphabet():
    for letter in string.ascii_lowercase:
        print(letter, end=' ')


lowercase_alphabet()


def uppercase_alphabet():
    for letter in string.ascii_uppercase:
        print(letter, end=' ')


uppercase_alphabet()


def digits():
    for letter in string.digits:
        print(letter, end=' ')


digits()


def symbols():
    symbol_characters = "@!#$%&*+-=?^~"

    for char in symbol_characters:
        print(char, end=' ')


symbols()
