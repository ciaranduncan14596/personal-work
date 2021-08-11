'''
Given a list of numbers, return whether any two sums to k. 
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

numbs = [ 10, 15, 3, 7 ]

def findACombination(array, numberToFind):
    for element in array:
        remainder = numberToFind - element
        if remainder in array:
            print (element, remainder)
            return True
    return False

print(findACombination(numbs, 18))