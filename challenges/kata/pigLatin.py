'''
Move the first letter of each word to the end of it, 
then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

'''

def pig_it(string):
    string_array = string.split(' ')
    new = []
    for word in string_array:

        if word.strip() in ['.', '!','?']:
            new.append(word)
        else:
            new.append(word[1:] + word[:1] +'ay')

    return ' '.join(new)

a = pig_it('Quis custodiet ipsos custodes ?') 
print(a)