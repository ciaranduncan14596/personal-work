'''
Scenario
Several people are standing in a row divided into two teams.
The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.

Task
Given an array of positive integers (the weights of the people), return a new array/tuple of two integers, 
where the first one is the total weight of team 1, and the second one is the total weight of team 2.
'''

def row_weights(array):
    row1 = 0
    row2 = 0

    for i in range (1, len(array)+1):
        print(i, i%2, array[i-1])
        if i % 2 == 0:
            row2 = row2 + array[i-1]
        else:
            row1 = row1 + array[i-1]

    return (row1, row2)

a = row_weights([100,51,50,100])
b = row_weights([100,50]) 
# 50, 51
# (150,151
print(a,b)