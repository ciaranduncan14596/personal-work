'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
'''

def underscoreToCamel(word):
    splitUp = word.split('-')
    splitUp = '_'.join(splitUp)
    splitUp = splitUp.split('_')

    print(splitUp)

    finalArray = [splitUp[0]]
    rest = splitUp[1:]
    for i in range(0, len(splitUp[1:])):
        finalArray.append(rest[i].capitalize())

    return ''.join(finalArray)
    

a = underscoreToCamel("the_pippi-Was_kawaii")
b = underscoreToCamel("A-cat_was_evil")
print(a)
print(b)
