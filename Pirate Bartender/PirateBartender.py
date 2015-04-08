__author__ = 'Ryan Kelley'
import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}


def get_answer():
    response = {}
    for key, value in questions.items():
        print(value)
        response[key] = input().lower() in ["y" or "yes"]
        print("")
    return response


def get_ingredients(response):
    drink = []
    for key, value in response.items():
        if not value:
            continue
        drink.append(random.choice(ingredients[key]))
    return drink


def main():
    response = get_answer()
    drink = get_ingredients(response)
    print("Here is your drink, ya fool!")
    print("here is what you ordered!: ")
    for i in drink:
        print("{}".format(i))


if __name__ == '__main__':
    main()
