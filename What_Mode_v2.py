def mode_type(question):
    while True:
        response = input(question).lower()
        if response in ["fs", "freestyle", "f"]:
            return "freestyle"
        elif response in ["s", "step-by-step", "step by step"]:
            return "step-by-step"
        elif response == "xxx":
            return "exit"
        else:
            print("Please enter 'Freestyle' or 'Step-by-step' (or 'xxx' to exit).")

def not_blank(question):
    # Checks that a user response is not blank

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")

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

def make_statement(statement, decoration):
    # Emphasises headings by adding decoration at the start and end

    return f"{decoration * 3} {statement} {decoration * 3}"

print()
what_mode = mode_type("What mode type would you like to use? (Freestyle or Step-by-step) ")

ingredients = []
brought = []
unit = []
needed = []
brought_total = []
price = []
making_cost = []

if what_mode == "freestyle":
    while True:
        freestyle_response = not_blank(
            "Enter response as: 'Name' 'Unit' 'Amount Brought' 'Amount Needed' 'Cost' (or 'xxx' to exit): "
        ).split()

        if freestyle_response[0].lower() == "xxx":
            break

        if len(freestyle_response) != 5:
            print("Please enter exactly 5 values: 'Name' 'Unit' 'Amount Brought' 'Amount_Needed' 'Cost' ")
            continue

        try:
            ingredient, unit_value, brought_amt, needed_amt, cost = freestyle_response
            ingredients.append(ingredient)
            unit.append(unit_value)
            brought_total.append(float(brought_amt))
            needed.append(float(needed_amt))
            price.append(float(cost))
        except ValueError:
            print("Please make sure that 'Amount Brought', 'Amount_Needed', and 'Cost' are numbers.")
            continue

elif what_mode == "step-by-step":
    while True:
        print()
        ingredient = not_blank("Name of ingredient? (Type 'xxx' to stop) ").strip()

        if ingredient.lower() == "xxx":
            break
        ingredients.append(ingredient)

        unit_value = unit_amount("What is the appropriate unit? ")
        unit.append(unit_value)

        if unit_value == "":
            food_amount = num_check(f"How many {ingredient}(s) do you need for the recipe? ")
            needed.append(food_amount)
        else:
            food_amount = num_check(f"How many {unit_value} of {ingredient}(s) do you need for the recipe? ")
            needed.append(food_amount)

    print()
    print(make_statement("Let's get the cost", '='))
    print()

    for ingredient in ingredients:
        brought_amount = num_check(f"How many {ingredient}(s) did you buy in total? ")
        brought_cost = num_check(f"How much did it cost you to buy {ingredient}? $")
        price.append(brought_cost)
        brought_total.append(brought_amount)

