'''
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

'''

def anagrams(word, list_of_words):
    dict_of_word = {}

    for letter in word:
        if letter not in dict_of_word:
            dict_of_word[letter] = 1
        else:
            dict_of_word[letter] = dict_of_word[letter] + 1

    list_of_anagrams = []
    for word in list_of_words:
        word_dict = {}
        for letter in word:
            if letter not in word_dict:
                word_dict[letter] = 1
            else:
                word_dict[letter] = word_dict[letter] + 1

        if word_dict == dict_of_word:
            list_of_anagrams.append(word)


    return list_of_anagrams

a = anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
b = anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
print(a,b )