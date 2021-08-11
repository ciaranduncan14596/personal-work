arrayA = [1,2,3,4,5]
arrayB = [6,7,2,3,9,3,12]

intersection = []
for element in arrayA:
    if element in arrayB:
        intersection.append(element)

print(intersection)

arrayC = [2,3,3,6,7,9,12]

print(set(arrayA).intersection(set(arrayC)))