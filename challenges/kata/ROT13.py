'''
How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc. Test examples:

rot13("EBG13 rknzcyr.") == "ROT13 example.";
rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"
'''



def rot13(string):
    print(string)
    new = ''
    chars = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for character in string:
        if character in chars:
            pos = chars.index(character)
            if pos > 13:
                new = new + chars[pos - 13]
            else: 
                new = new + chars[13 + pos]
        elif character in 'ABCDEFGHIJKLMNOPQRSTUVQXYZ':
            pos = chars.index(character.lower())
            if pos >= 13:
                new = new + chars[pos - 13].upper()
            else: 
                new = new + chars[13 + pos].upper()
        else:
            new = new + character
    return new

a = rot13("(.y<W~/7;A#") 
print(a)