import sys

if len(sys.argv) != 2 or sys.argv[1].isdigit() == False:
    print("ERROR", end="")
else:
    num = int(sys.argv[1])
    if num == 0:
        print("I'm Zero.", end="")
    elif (num) % 2 == 0:
        print("I'm Even.", end="")
    else:
        print("I'm Odd.", end="")
