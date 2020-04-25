import sys

if len(sys.argv) != 3 or sys.argv[1].isdigit() == True or sys.argv[2].isdigit() == False:
    quit(print("ERROR", end=""))

str_splited = sys.argv[1].split(" ")
list =[]
for word in str_splited:
    if len(word) > int(sys.argv[2]):
        list.append(word)
print(list)