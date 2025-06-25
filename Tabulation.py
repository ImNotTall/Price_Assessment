import pandas
from tabulate import tabulate

def not_blank(question):
    # Checks that a user response is not blank

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")

apples = []
bananas =[]
melons = []
grapes = []
oranges = []

final_dict = {
    "Apple": apples,
    "Banana": bananas,
    "Melon": melons,
    "Grape": grapes,
    "Orange": oranges,
}

apple_amount = not_blank("How many Apples do you need? ")
apples.append(apple_amount)
banana_amount = not_blank("How many Bananas do you need? ")
bananas.append(banana_amount)
melon_amount = not_blank("How many Melons do you need? ")
melons.append(melon_amount)
grape_amount = not_blank("How many Grapes do you need? ")
grapes.append(grape_amount)
orange_amount = not_blank("How many Oranges do you need? ")
oranges.append(orange_amount)

final_frame = pandas.DataFrame(final_dict)

food_results = tabulate(final_frame[['Apple', 'Banana', 'Melon', 'Grape', 'Orange']], headers='keys',
                          tablefmt='psql', showindex=False)

print(f"Your Items: \n{food_results}")