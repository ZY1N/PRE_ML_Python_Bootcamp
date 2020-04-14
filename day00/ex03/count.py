import string

def go_analyze(text):
    wordcount, upper, lower, punctuation, spaces = (0,) * 5
    for character in text:
        if(character.islower()):
            lower += 1
        if(character.isupper()):
            upper += 1
        if(character in string.punctuation):
            punctuation += 1
        if(character.isspace()):
            spaces += 1
        wordcount += 1
    print("The text contains ", wordcount, " characters:")
    print("- ", upper, "upper letters")
    print("- ", lower, "lower letters")
    print("- ", punctuation, "punctuation marks")
    print("- ", spaces, "spaces")

def text_analyzer(text = None):
    '''This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.'''
    if(text == None):
        text = input("What is the text to analyse?\n")
    go_analyze(text)