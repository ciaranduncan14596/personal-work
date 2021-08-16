'''
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
'''

def alphabet_position(string):
    letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    lettersArray = letters.split(' ')
    letterDict = {}

    for i in range(0, len(lettersArray)):
        letterDict[lettersArray[i]] = i+1

    arrayNums = []

    string = string.lower().replace(' ', '')
    for character in string:
        if character in letterDict.keys():
            arrayNums.append(str(letterDict[character]))
    return ' '.join(arrayNums)

a = alphabet_position("The sunset sets at twelve o' clock.")
print(a)
