import pandas
from tabulate import tabulate


def make_statement(statement, decoration):
    # Emphasises headings by adding decoration at the start and end

    return f"{decoration * 3} {statement} {decoration * 3}"


def yes_no_check(question):
    # Checks that users enter yes / y or no / n to a question

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n). \n")


def instructions():
    print(make_statement("Instructions", "🔎"))

    # Instructions to help user understand the program and questions

    print(''' 
You will be asked a series of questions:

The recipe name.
Number of servings.
What mode you would like to select:

Freestyle:
Freestyle will allow you to enter one big line of input data. However each variable must be in order or the code will not accept the answer!
This mode is recommend to experts who know what their doing or to people who want to be quick.

step-by-step:
Step-by-step is recommend to people who are using the program for the first time or have difficulty with computers.
This mode will ask questions in order. It does not allow you to enter your response all at once.
Questions asked in step-by-step include:

Name of ingredient.
The appropriate unit.
How many of that particular ingredient for the recipe.

Both modes will repeat itself until you enter the break key: "xxx" .

Only 'Step-by-step' will ask for how many bought and the cost of all the ingredients entered.
If your using 'Freestyle' you will need to enter how many brought and the cost at the same time as every other variable.

Once all ingredients have been inputted, the code will display in a graph the results.

At the bottom of the page, the cost per serving can be found as well as the total cost.

    ''')


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


def currency(x):
    return "${:.2f}".format(x)

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

fixed_subtotal = 0
fixed_panda_string = ""

# Main routine starts here

print(make_statement("Recipe Calculator", "🥞"))

print()
want_instructions = yes_no_check("Do you want to see the instructions? ")
print()

# Displays instructions if user enters 'yes'
if want_instructions == "yes":
    instructions()

# Asks questions to get information on recipe items
recipe_name = not_blank("Recipe Name: ")
servings = num_check("Number of servings needed? ")

what_mode = mode_type("What mode type would you like to use? (Freestyle or Step-by-step) ")

# Lists to store inputs
ingredients = []
brought = []
unit = []
needed = []
brought_total = []
price = []
making_cost = []

# Used for final tabulation
final_dict = {
    "Ingredient": ingredients,
    "Amount Needed": needed,
    "Amount Brought": brought_total,
    "Unit": unit,
    "Price": price,
    # "Cost to Make": making_cost
}

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

#  Maths for displaying data
total_cost_brought = sum(cost for _, cost in brought)

final_frame = pandas.DataFrame(final_dict)

final_frame['Cost to Make'] = final_frame['Price'] / final_frame['Amount Brought'] * final_frame['Amount Needed']
absolute_total = final_frame['Cost to Make'].sum()

add_dollars = ['Cost to Make', 'Price']

for var_item in add_dollars:
    final_frame[var_item] = final_frame[var_item].apply(currency)

cost_per_serving = f"{absolute_total / servings:.2f}"

# Displays data user has imputed
recipe_results = tabulate(final_frame[['Ingredient', 'Amount Needed', 'Amount Brought', 'Price', 'Unit',
                                       'Cost to Make']], headers='keys',
                          tablefmt='psql', showindex=False)

# Displays final cost and cost per serving
print()
print(make_statement(f"{recipe_name}", "="))
print(f"Servings: {servings}")
print()
# TODO: Remove "\n" for trialling. Add back after screenshotted
print(f"The total cost of items brought: \n{recipe_results}")
print()
print(f"Total: {absolute_total:.2f}")
print(f"The total cost per serving: ${cost_per_serving}")
