import string

VALID_ENDINGS =  ['.', '?', '!']
INVALID_NUMBERS = ['1','2','3','4','5','6','7','8', '9', '10', '11','12']

def sentence_validator(sentence):
    # Controller for Sentence Validation
    if len(sentence) > 0:
        if (
            validate_first_character(sentence) 
            and validate_ending(sentence) 
            and validate_quotations(sentence)
            and validate_full_stops(sentence)
            and validate_numerals(sentence)
        ):
            return True
    return False
    

def validate_first_character(sentence):
    # Validate first character is a capital letter
    if len(sentence) > 0:
        return sentence[0].isupper()
    return False

def validate_ending(sentence):
    # Validate last character is a valid ending
    if len(sentence) > 0:
        return sentence[len(sentence)-1] in VALID_ENDINGS
    return False

def validate_quotations(sentence):
    if len(sentence) > 0:
        return sentence.count('"') % 2 == 0
    return False

def validate_full_stops(sentence):
     # validate the number of full stops if they exist
    if len(sentence) > 0:
        if '.' in sentence:
            return sentence.index('.') == len(sentence) -1
        return True
    return False

def validate_numerals(sentence):
    # validate numerals below 13 are in sentence format
    if len(sentence) > 0 :
        words_without_punctuation = ''.join(
            ch for ch in sentence if ch not in set(string.punctuation)
            ).split(' ')
        numbers_in_list = [word for word in words_without_punctuation if word in INVALID_NUMBERS]
        return len(numbers_in_list) == 0
    return False


if __name__ == '__main__':
    print('Please enter your sentence: \n')
    sentence = input()
    is_valid = sentence_validator(sentence)
    if is_valid:
        print('Your sentence is valid')
    else:
        print('Your Sentence is invalid')