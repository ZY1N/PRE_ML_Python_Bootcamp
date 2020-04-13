import sys

def error(length):
    if(length != 1):
        print("ERROR")
    exit()

def main():
    if(len(sys.argv) != 2):
        error(len(sys.argv))
    var = sys.argv[1]
    if(var.isnumeric() == False):
        error(len(sys.argv))
    if (int(var) == 0):
        print("I'm Zero.")    
    elif(int(var) % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()