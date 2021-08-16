'''
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should 
replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
'''

def solution(string):
    array = []
    if len(string) % 2 == 1:
        string = string+ '_'
    for i in range(0, len(string),2):
        newStr = string[i]+ string[i+1]
        array.append(newStr)
    
    return array

a = solution('abc')
b = solution('abcdef')
print(a,b)