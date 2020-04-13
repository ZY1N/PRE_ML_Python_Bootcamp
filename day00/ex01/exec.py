import sys

def main():
    if (len(sys.argv) > 1):
        output = sys.argv[1:]
        #concatonate the list and swap the case
        output = (' '.join(output)).swapcase()
        #reversed goes through the string from the last index to first
        #join the reversed into a string
        output = ''.join(reversed(output))
        print(output)

if __name__ == "__main__":
    main()