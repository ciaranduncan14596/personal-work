
'''
Assign every lowercase letter a value, 
from 1 for a to 26 for z. Given a string of lowercase letters, 
find the sum of the values of the letters in the string.
'''

letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
lettersArray = letters.split(' ')
letterDict = {}

for i in range(0, len(lettersArray)):
    letterDict[lettersArray[i]] = i+1


def wordSummerUpper(word, dictionary):
    counter = 0
    for letter in word:
        counter += dictionary[letter]
    return counter

wordSum = wordSummerUpper('zebra', letterDict)
print(wordSum)