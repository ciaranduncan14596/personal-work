'''
Given a sorted array of distinct integers, write a function index_equals_value that returns the lowest index for which array[index] == index.
Return -1 if there is no such index.

Your algorithm should be very performant.

[input] array of integers ( with 0-based nonnegative indexing )
[output] integer

Examples:
input: [-8,0,2,5]
output: 2 # since array[2] == 2

input: [-1,0,3,6]
output: -1 # since no index in array satisfies array[index] == index
'''

def index_equals_value(arr):
    if arr[0] <= 0 and arr
    for val in arr:
        if val == arr.index(val):
            return val
    return -1
    
    return -1 if len(non_negs) == 0 else non_negs[0]

    

a = index_equals_value([-8,0,2,5])
print(a)