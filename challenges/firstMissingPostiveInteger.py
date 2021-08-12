"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
You can modify the input array in-place.
Example:
>>> coding_problem_04([3, 4, -1, 1])
2
>>> coding_problem_04([1, 2, 0])
3
>>> coding_problem_04([4, 1, 2, 2, 2, 1, 0, 5])
3
"""

def firstMissingPositiveInteger(arr):
    arr.sort()
    print(arr)

    counter = 1

    for number in arr:
        if number == counter:
            counter = counter + 1

    print(counter)

firstMissingPositiveInteger([3, 4, -1, 1])