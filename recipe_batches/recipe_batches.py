#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # set dictionary
    dictionary_recipe = recipe
    dictionary_ingredient = ingredients
    # set total batches to none
    batches_total = None

    # check if key exists in ingredient direct
    for key in dictionary_recipe.keys():
        # if not then the batches is 0 and return
        if key not in dictionary_ingredient:
            return 0
        batches = dictionary_ingredient[key]//dictionary_recipe[key]
        if batches == 0:
            return 0
        # compare batches_total with batches
        if not batches_total:
            batches_total = batches
        else:
            batches_total = min(batches_total, batches)

    return batches_total


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
