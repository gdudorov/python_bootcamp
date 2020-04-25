import datetime
from recipe import Recipe

class Book:
    """
    • name (str)
    • last_update (datetime)
    • creation_date (datetime)
    • recipes_list (dict) : a dictionnary why 3 keys: “starter”, “lunch”, “dessert”.
    """
    name = "Name of the cooking book"
    #last_update = datetime.datetime
    #creation_date = datetime.datetime
    recipes_list = {
                    'starter': {'Name': 'sandwich',  'Ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],        'Level': "1", 'Time': "10", 'Description': 'Fast and yami' },
                    'lunch':   {'Name': 'salad',     'Ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'Level': "2", 'Time': "15", 'Description': 'Greens are always good !' },
                    'dessert': {'Name': 'cake',      'Ingredients': ['flour', 'sugar', 'eggs'],                    'Level': "3", 'Time': "45", 'Description': 'Just get a tea or cofee!' },
                   }
    def __init__(self, name):
        self.name = name if isinstance(name, str) and name != "" else quit(print("Incorrect input of the CookingBook Name, with value of ", name, ". Please restart and try again"))

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for n in self.recipes_list:
           # print(self.recipes_list[n]['Name'])
            if self.recipes_list[n]['Name'] == name:
                rln = self.recipes_list[n]             #shortener
                tmp_recipe = Recipe(rln['Name'],rln['Level'],rln['Time'],rln['Ingredients'],rln['Description'], n)
                print(str(tmp_recipe))
                return(tmp_recipe)
        return(print("NO SUCH AS RECIPE IN THE COOKBOOK"))
    pass

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for key in self.recipes_list.keys():
           #print(self.recipes_list[key]['Name'])
            if key == recipe_type:
                return(print(self.recipes_list[key]['Name']))
        return(print("NO DATA OR THE RECIPE TYPE:",recipe_type))
    pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        #You will have to handle the error if the arg passed in add_recipe is not a Recipe.

        self.recipes_list[recipe.recipe_type] = {'Name': recipe.name, 'Ingredients': recipe.ingredients,'Level': recipe.cooking_lvl, 'Time': recipe.cooking_time, 'Description': recipe.description} if isinstance(recipe, Recipe) else quit(print("INCORRECT RECIPE DATA TYPE"))
        #print(self.recipes_list)

    pass


