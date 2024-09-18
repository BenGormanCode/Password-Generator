import random


class Generator:
    def __init__(self, password_length, answers):
        self.length = password_length
        self.answers = answers
        self.per_category = password_length / len(answers)

    def generate(self):
        print(
            f"The length is {self.length} and it will use {self.per_category} characters per category.")
