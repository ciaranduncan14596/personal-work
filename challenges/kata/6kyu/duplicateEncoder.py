'''
The goal of this exercise is to convert a string to a new string where each character in the new string is
 "(" if that character appears only once in the original string, or ")" 
 if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes

Assertion messages may be unclear about what they display in some languages. 
If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!
'''


def duplicate_encode(word):
    word_list = [ x for x in word.lower()]
    word_dict = {}

    for letter in word_list:
        if letter in word_dict:
            word_dict[letter] = word_dict[letter] + 1
        else:
            word_dict[letter] = 1



    new_string = ''
    for letter in word_list:
        if word_dict[letter] > 1:
            new_string = new_string + ")"
        else:
            new_string = new_string + '('

    return new_string
duplicate_encode('Success')