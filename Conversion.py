def convert_units(needed_amt, unit_needed, unit_brought):
    abbreviations = {
        "g": "grams",
        "kg": "kilograms",
        "ml": "millilitres",
        "l": "litres"
    }

    unit_needed = abbreviations.get(unit_needed.lower(), unit_needed.lower())
    unit_brought = abbreviations.get(unit_brought.lower(), unit_brought.lower())

    # Conversions
    conversions = {
        ("grams", "kilograms"): needed_amt / 1000,
        ("kilograms", "grams"): needed_amt * 1000,
        ("millilitres", "litres"): needed_amt / 1000,
        ("litres", "millilitres"): needed_amt * 1000
    }

    if unit_needed == unit_brought:
        return needed_amt
    elif (unit_needed, unit_brought) in conversions:
        return conversions[(unit_needed, unit_brought)]
    elif (unit_brought, unit_needed) in conversions:
        # Convert to match unit_brought regardless of input order
        return conversions[(unit_brought, unit_needed)]
    # User must input a response that is able to be converted from unit to unit
    else:
        print(f"⚠️ Units '{unit_needed}' and '{unit_brought}' are not compatible. No conversion applied.")
        return needed_amt

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

def make_statement(statement, decoration):
    """ Emphasises headings by adding decoration at the start and end """

    return f"{decoration * 3} {statement} {decoration * 3}"

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

ingredients = []
brought = []
unit = []
needed = []
brought_total = []
price = []
making_cost = []

while True:
    print()
    # If the user type "xxx" the code will break and continue to the next section
    ingredient = not_blank("Name of ingredient? (Type 'xxx' to stop) ").strip()

    if ingredient.lower() == "xxx":
        break
    ingredients.append(ingredient)

    # Asks for appropriate unit from a list
    unit_value = unit_amount("What is the appropriate unit? ")
    unit.append(unit_value)

    # If the food item is an item that doesn't have a unit (E.g. Eggs) it will ignore the "Units" part of the question
    if unit_value == "":
        food_amount = num_check(f"How many {ingredient}(s) do you need for the recipe? ")
        needed.append(food_amount)
    # Asks for the amount of ingredients for recipe
    else:
        food_amount = num_check(f"How many {unit_value} of {ingredient}(s) do you need for the recipe? ")
        needed.append(food_amount)

print()
print(make_statement("Let's get the cost", '='))
print()

for i, ingredient in enumerate(ingredients):
    brought_amount = num_check(f"How many {ingredient}(s) did you buy in total? ")
    unit_brought = input(f"What unit did you buy {ingredient} in? ").lower().strip()
    brought_cost = num_check(f"How much did it cost you to buy {ingredient}? $")

    # Convert the amount needed to match the unit bought
    adjusted_amt = convert_units(needed[i], unit[i], unit_brought)
    needed[i] = adjusted_amt
    unit[i] = unit_brought  # Override the unit to match

    price.append(brought_cost)
    brought_total.append(brought_amount)

