'''
https://www.codewars.com/kata/55c04b4cc56a697bb0000048/python
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
'''

def scramble(letters, word):

    letter_dict = {}
    word_dict = {}
    for letter in letters:
        if letter in letter_dict:
            letter_dict[letter] = letter_dict[letter] +1
        else:
            letter_dict[letter] = 1

    for letter in word:
        if letter in word_dict:
            word_dict[letter] = word_dict[letter] +1
        else:
            word_dict[letter] = 1

    word_checker = []
    for i in word_dict.keys():
        if i not in letter_dict.keys():
            word_checker.append(False)
        elif letter_dict[i] < word_dict[i]:
            word_checker.append(False)
    
    if False in word_checker:
        return False
    return True

a = scramble('cedewaraaossoqqyt', 'codewars')
print(a)