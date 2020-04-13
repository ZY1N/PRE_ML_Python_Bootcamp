import string

def text_analyzer(text):
    upper, lower, punctuation, spaces = 0
    for character in text:
        if(isLowerCase(character)):
            lower++
        if(isUpperCase(character)):
            upper++
        if(character in string.punctuation):
            punctuation++
        if(isspace(character))
            spaces++
    print("The text contains ", wordcount, " characters:")
    print("- ", upper, "upper letters")
    print("- ", lower, "lower letters")
    print("- ", punctuation, "punctuation marks")
    print("- ", spaces, "spaces")

