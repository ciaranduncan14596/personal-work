'''
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" 
is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. 
Return True if it is, False if not. Ignore numbers and punctuation.
'''

def is_pangram(string):
    string = string.lower().replace(' ', '').replace('.','').replace(',', '')
    lettersArr = []
    for character in string:
        if character not in lettersArr and not character.isnumeric():
            lettersArr.append(character)
    if len(lettersArr) == 26:
        lettersArr.sort()

        return True
    return False

# a = is_pangram('The quick brown fox jumps over the lazy dog')
b = is_pangram('ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ')
# print(a)
print(b)