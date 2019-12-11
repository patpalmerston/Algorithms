#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batches = []
    # find keys and make sure that recipe and ingredients have matching values
    if recipe.keys() == ingredients.keys():
        for key in recipe:
          #divide each key value bye the corresponding value... ingredient amount needs to be more than what recipe needs
            batches.append(ingredients[key] // recipe[key])
            #round down to whole number
            return min(batches)

    else:
      #if there the recipe and ingredient key values dont match then no recipe
        return 0


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))