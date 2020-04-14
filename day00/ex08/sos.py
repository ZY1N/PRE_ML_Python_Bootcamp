import sys

MorseDictionary = {' ': '_', 
	"'": '.----.', 
	'(': '-.--.-', 
	')': '-.--.-', 
	',': '--..--', 
	'-': '-....-', 
	'.': '.-.-.-', 
	'/': '-..-.', 
	'0': '-----', 
	'1': '.----', 
	'2': '..---', 
	'3': '...--', 
	'4': '....-', 
	'5': '.....', 
	'6': '-....', 
	'7': '--...', 
	'8': '---..', 
	'9': '----.', 
	':': '---...', 
	';': '-.-.-.', 
	'?': '..--..', 
	'A': '.-', 
	'B': '-...', 
	'C': '-.-.', 
	'D': '-..', 
	'E': '.', 
	'F': '..-.', 
	'G': '--.', 
	'H': '....', 
	'I': '..', 
	'J': '.---', 
	'K': '-.-', 
	'L': '.-..', 
	'M': '--', 
	'N': '-.', 
	'O': '---', 
	'P': '.--.', 
	'Q': '--.-', 
	'R': '.-.', 
	'S': '...', 
	'T': '-', 
	'U': '..-', 
	'V': '...-', 
	'W': '.--', 
	'X': '-..-', 
	'Y': '-.--', 
	'Z': '--..', 
	'_': '..--.-'}

def main():
    flag = 0
    backslashflag = 0
    morsemessage = ""
    for argument in sys.argv:
        if(backslashflag == 1):
            morsemessage += "/"
            backslashflag = 0
        if(flag == 0):
            flag = 1
        elif(flag == 1):
            for letter in argument:
                letter = letter.upper()
                if(backslashflag == 1):
                    morsemessage += "/"
                    backslashflag = 0
                if(not letter.isalnum() and not letter.isspace()):
                    print("ERROR")
                    exit()
                else:
                    if(letter.isspace()):
                        backslashflag = 1
                    else:
                        morsemessage += MorseDictionary[letter]
                morsemessage += " "
            backslashflag = 1
    print(morsemessage)

if (__name__ == "__main__"):
    main()
