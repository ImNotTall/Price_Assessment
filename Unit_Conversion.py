import pandas
from tabulate import tabulate

def not_blank(question):
    # Checks that a user response is not blank

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")

def num_check(question, num_type="float", exit_code=None):
    # Checks if the user has entered more than 0

    if num_type == "float":
        error = "Oops - Please enter an integer more than zero."
    else:
        error = "Oops - Please enter a number more than zero"

    while True:

        response = input(question)

        if response == exit_code:
            return response

        try:

            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def unit_amount(question, num_letters=1):
    # Lists of appropriate units
    unit_list = ['grams', 'kilograms', 'litres', 'millilitres', 'drops']

    while True:
        # If the user enters the appropriate unit, the program will continue. If not, the program will ask again
        response = input("What is the appropriate unit? ").lower()

        # The user may press 'enter' to not add a unit as certain item require it (E.g. Eggs)
        if response == "":
            return ""

        for item in unit_list:

            if response == item:
                return item
            elif response == item[:num_letters]:
                return item
            if response == "kg":
                return "kilograms"
            if response == "ml":
                return "millilitres"

        else:
            print(f"Please enter an appropriate unit from {unit_list} or its abbreviation")
            print()

