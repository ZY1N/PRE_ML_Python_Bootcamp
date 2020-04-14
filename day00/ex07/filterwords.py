import sys
import re

def error():
    print("ERROR")
    exit()

# def gofilter(wrdlen, listofwrd):
    # for wrd in listofwrd:
    #     if(len(wrd) > wrdlen)

def main():
    if(len(sys.argv) != 3):
        error()
    else:
        nbr = sys.argv[2]
        if(sys.argv[1].isnumeric()):
            error()
        if(not nbr.isnumeric()):
            error()
        else:
            filteredstuff = [wrd for wrd in (re.sub(r'[^\w\s]','',sys.argv[1])).split() if len(wrd) > int(nbr)]
            print(filteredstuff)

if(__name__ == "__main__"):
    main()
