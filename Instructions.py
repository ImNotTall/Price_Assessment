
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

def make_statement(statement, decoration):
    # Emphasises headings by adding decoration at the start and end

    return f"{decoration * 3} {statement} {decoration * 3}"

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

print()
instructions_wanted = yes_no_check("Would you like to see the instructions?" )

if instructions_wanted == "yes":
    instructions()