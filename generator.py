import random


class Generator:
    def __init__(self, password_length, answers):
        self.length = password_length
        self.answers = answers
        self.per_category = password_length / len(answers)

    def generate(self):
        print(
            f"Password length: {self.length} | Per Category: {self.per_category} | Answers: {self.answers}")

    def pick(self):
        output = []

        # for each choice, return a self.per_catergoy sample of the category string
        for category in self.answers:
            # if category == uppers
            # make and array of uppers
            # take a random.sample of length self.percategory
            # join the selected characters to output

            ### your code ###

            # if category == lowerd
            # make and array of lower
            # take a random.sample of length self.percategory
            # join the selected characters to output

            ### your code ###

            # if category == numbers
            # make and array of numbers
            # take a random.sample of length self.percategory
            # join the selected characters to output

            ### your code ###

            # if category == symbols
            # make and array of symbols
            # take a random.sample of length self.percategory
            # join the selected characters to output
            # --- watch out - if you sample more then the number of symbols available i don't know what will happen maybe an error

            ### your code ###

        return output
