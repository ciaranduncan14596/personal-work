def count_smileys(array):
    count = 0

    for character in array:
        if len(character) == 2:
            if character[0] in [':', ';'] and character[1] in [')', 'D']:
                count = count + 1
        if len(character) == 3:
            if character[0] in [':', ';'] and character[1] in ['-', '~'] and character[2] in [')', 'D']:
                count = count + 1


    return count

a = countSmileys([':)', ';(', ';}', ':-D'])   
b = countSmileys([';D', ':-(', ':-)', ';~)'])
c = countSmileys([';]', ':[', ';*', ':$', ';-D'])

print(a,b,c)