def square_digits(number):
    newArray = []
    numberStr = str(number)
    for digit in numberStr:
        asNumber = int(digit) * int(digit)
        newArray.append(str(asNumber))

    appendedStr = ''.join(newArray)
    return int(appendedStr)

number = square_digits(1234)
print(number)