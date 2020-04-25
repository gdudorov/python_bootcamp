from book import Book
from recipe import Recipe
tourte = Recipe("Pirojok","2", "360",["flour","egg","yeast","butter","salt","sugar","stuffing"], "Mix flour and eggs...Or just call wife and do nothing: relax with beer in front of TV", "snack")
to_print = str(tourte)
print(to_print)

cooking_book = Book("Tatarskaya")
cooking_book.add_recipe(tourte)
recipe_of_cake = cooking_book.get_recipe_by_name("cake")
print(str(recipe_of_cake))
cooking_book.get_recipes_by_types("starter")




"""
• name (str)
• cooking_lvl (int) : range 1 to 5
• cooking_time (int) : in minutes (no negative numbers)
• ingredients (list) : list of all ingredients each represented by a string
• description (str) : description of the recipe
• recipe_type (str) : can be “starter”, “lunch” or “dessert”.
"""