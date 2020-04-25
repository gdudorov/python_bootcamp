import random

print ("This is an interactive guessing game!\n"
"You have to enter a number between 1 and 99 to find out the secret number.\n"
"Type 'exit' to end the game.\n"
"Good luck!")
rand = random.randint(1,99)
print (rand)
count = 0
while True:
    count =count + 1
    num =  input("What's your guess between 1 and 99? ")
    if (num == 'exit'):
        quit(print("Goodbuy!"))
    elif num.isdigit() == False :
        print("That's not a number.", end="")
        break
    elif int(num) == rand:
        if int(num) == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if count == 1:
            quit(print("Congratulations! You got it on your first try!", end=""))
        else:
            quit(print("Congratulations, you've got it! \n"
             "You won in", count,"attempts!", end=""))
    elif int(num) > rand:
        print("Too high!")
    else: print("Too low!")

