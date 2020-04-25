class Recipe():
    name= "No name"
    cooking_lvl = int(1)
    cooking_time = int(0)
    ingredients = ["list of all ingredients", "including wife or girlfriend"]
    description = "do nothing, just relax!"
    recipe_type = "starter"

    def __init__(self,name,cooking_lv,cooking_time,ingredients, description,recipe_type):
        self.name = name if isinstance(name, str) and name !="" else quit(print("Incorrect input of the recipy Name, with value of ",name,".PLEASE RESTART AND TRY AGAIN(name)"))
        self.cooking_lvl = int(cooking_lv) if isinstance(cooking_lv, int) or cooking_lv.isdigit() and int(cooking_lv) in range(1,6) else quit(print("Incorrect input of the Cooking level (1-5), with value of ",cooking_lv,".PLEASE RESTART AND TRY AGAIN(cooking_lv)"))
        self.cooking_time = int(cooking_time) if isinstance(cooking_time, int) or cooking_time.isdigit() else quit(print("Incorrect input of the Cooking time (minutes), with value of ", cooking_time, ".PLEASE RESTART AND TRY AGAIN (cooking_time)"))
        self.ingredients = ingredients if isinstance(ingredients, list) and list !="" else quit(print("Incorrect input of the List of ingredients, with value of ",ingredients,".PLEASE RESTART AND TRY AGAIN(ingedients)"))
        self.description = description
        self.recipe_type = recipe_type if isinstance(recipe_type, str) and recipe_type == "starter" or "lunch" or "dessert" else quit(print("Incorrect input of the recipe Type, with value of",recipe_type,".PLEASE RESTART AND TRY AGAIN(recipe_type)"))


    def __str__(self):
        "Return the string to print with the recipe info"
        txt =""
        """Your code goes here"""
        ingr =""
        for i in self.ingredients:
            ingr += i + (", " if self.ingredients.index(i)+1 != len(self.ingredients) else ".")
        txt = "Name: " + self.name + "\nCooking level: " + str(self.cooking_lvl) + "\nCooking time: " + str(self.cooking_time) + "\nList of ingeredients: " + ingr + "\nDescription(optional): " + self.description + "\nType of recipe: "+self.recipe_type
        return txt

"""
• name (str)
• cooking_lvl (int) : range 1 to 5
• cooking_time (int) : in minutes (no negative numbers)
• ingredients (list) : list of all ingredients each represented by a string
• description (str) : description of the recipe
• recipe_type (str) : can be “starter”, “lunch” or “dessert”.
"""