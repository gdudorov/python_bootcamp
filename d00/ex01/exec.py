import sys
#if len(sys.argv) == 1:
#    print("", end="")
for i in range(len(sys.argv), 1, -1):
    print((sys.argv[i - 1][::-1]).swapcase(), end="")
    if i-1 != 1:
        print(" ", end="")
print("", end ="")

