import sys
if len(sys.argv) < 3:
    quit(print("InputError: too less arguments"))
elif len(sys.argv) > 3:
    quit(print("InputError: too many arguments"))
elif (sys.argv[1].isdigit() and sys.argv[2].isdigit()) == False:
    quit(print("InputError: only numbers\n\nUsage: python operations.py <number1> <number2>\nExample:\n   python operations.py 10 3"))
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("Sum:        ",a+b)
    print("Difference: ",a-b)
    print("Product:    ",a*b)
    print("Quotient:   ","ERROR (div by zero)" if b == 0 else a/b)
    print("Remainder:  ","ERROR (modulo by zero)" if b == 0 else a%b)