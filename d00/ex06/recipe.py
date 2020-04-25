cb= {
'sandwich': {'ingr': ('ham', 'bread', 'cheese', 'tomatoes'), 'meal' : 'lunch','time' : 10},
'cake': {'ingr':('flour', 'sugar', 'eggs'), 'meal' : 'dessert', 'time' : 60},
'salad': {'ingr': ('avocado', 'arugula', 'tomatoes', 'spinach'),'meal' : 'lunch','time' : 15}}

#function to add a new recipe to cookbook with its ingredients, its meal type and its preparation
#time. The function parameters will be: name of recipe, ingredients, meal and prep_time
def add_rec(rec_name, ingr, meal, time):
    cb[rec_name] = {'ingr': ingr, 'meal': meal, 'time': time}
    print(cb)
#function to delete a recipe from the dictionary. The function parameter will be: name of the recipe
def del_rec(rec_name):
    del cb[rec_name]
    print(cb)

#function to print all recipe names from cookbook. Think about formatting the output
def print_rec (rec_name):
    print(cb[rec_name])
def print_cb():
    print(cb)

#program using the four functions you just created. The program will prompt the
#user to make a choice between printing the cookbook, printing only one recipe, adding a recipe, deleting a
#recipe or quitting the cookbook.

# print(*cb)
# print_rec('sandwich')
# del_rec('sandwich')
# add_rec('omlet', ('eggs','sosage', 'milk', 'spices','tomatos'), 'breakfast', 20)
# print_rec('omlet')

print ("Please select an option by typing the corresponding number: \n"
"1: Add a recipe\n"
"2: Delete a recipe\n"
"3: Print a recipe\n"
"4: Print the cookbook\n"
"5: Quit")

k = input()
if k=='1':
    print("Please enter the recipe's name and its details (name, meal, time, (ingrs1,ingr2...ingrN):", end=' ')
    name,meal,time = input().split(",")
    ingr = list(input().split(","))
    add_rec(name, ingr, meal, int(time))
 # add_rec('omlet', ('eggs', 'sosage', 'milk', 'spices', 'tomatos'), 'breakfast', 20)
elif k == '2':
    name=input("Please enter the recipe's name to delete")
    del_rec(name)
elif k == '3':
    print(*cb)
    print_rec(input("Please enter which recipe you want to see: "))
elif k == '4':
    print_cb()
elif k == '5':
    quit(print('Thank you, see you again !'))