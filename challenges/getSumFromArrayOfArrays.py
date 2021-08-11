array = [1,2, [8,9,[4, [12, 16, 11], [15]]]]

def getSumFromArrayOfArrays(arr, counter):
    for thing in arr:
        if type(thing) == int:
            counter+=thing
        else:
            counter = getSumFromArrayOfArrays(thing, counter)
    return counter


counter = getSumFromArrayOfArrays(array, 0)
print(counter)