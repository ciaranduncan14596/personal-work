"""
    Given a stack of N elements, interleave the first half of the stack
    with the second half reversed using one other queue.
    Example:
    >>> coding_problem_01([1, 2, 3, 4, 5])
    [1, 5, 2, 4, 3]
    >>> coding_problem_01([1, 2, 3, 4, 5, 6])
    [1, 6, 2, 5, 3, 4]
    Note: with itertools, you could instead islice(chain.from_iterable(izip(l, reversed(l))), len(l))
    """

def interleaveStack(stack):
    newArray = []
    reversedStack = stack[::-1]

    middleElement = len(stack) / 2
    remainder = len(stack) % 2

    i = 0
    j = 0
    while i <= middleElement and j < middleElement:
        newArray.append(stack[i])
        newArray.append(reversedStack[j])
        i+=1
        j+=1

    if remainder == 1:
        newArray.append(stack[middleElement])
    print(newArray)       

interleaveStack([1, 2, 3, 4, 5])
interleaveStack([1, 2, 3, 4, 5, 6])