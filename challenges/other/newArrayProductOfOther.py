'''
Given an array of integers, return a new array such that each element at index i of the new array 
is the product of all the numbers in the original array except the one at i. 
Example:
>>> coding_problem_02([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]
'''

array = [1,2,3,4,5]

newArray = []


for i in range(0, len(array)):
    counter = 1
    array1 = array[0:i]
    array2 = array[i+1:len(array)]
    for number in array1:
        counter = counter * number
    for number in array2:
        counter = counter * number
    newArray.append(counter)

print(newArray)