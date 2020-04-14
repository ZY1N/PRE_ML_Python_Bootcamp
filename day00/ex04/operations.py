import sys
import types

def formatnum(nbr):
    if(isinstance(nbr, str)):
        return(nbr)
    if(nbr % 1 == 0):
        return(int(nbr))
    else:
        return(nbr)


def docalc(lst):
    add, sub, prod, quot, remain = (0,) * 5
    if(not lst[1].isnumeric() or not lst[2].isnumeric()):
        print("InputError: only numbers\n")
        print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
        exit()
    first = float(lst[1])
    second = float(lst[2])
    add = first + second
    sub = first - second
    prod = first * second
    if(second != 0):
        quot = first / second
        remain = first % second
    else:
        quot = "ERROR (div by zero)"
        remain = "ERROR (modulo by zero)"
    #use ljust to align it
        #string method to left justify
    print("Sum:".ljust(11, " "), formatnum(add))
    print("Difference:".ljust(11, " "), formatnum(sub))
    print("Product:".ljust(11, " "), formatnum(prod))
    print("Quotient:".ljust(11, " "), formatnum(quot))
    print("Remainder:".ljust(11, " "), formatnum(remain))

def main():
    length = len(sys.argv)
    if(length == 1 or length == 2):
        print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
        exit()
    elif(length == 3):
        docalc(sys.argv)
    else:
        print("InputError: too many arguments\n")
        print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
        exit()

if __name__ == "__main__":
    main()