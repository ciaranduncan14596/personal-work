'''
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order.
 Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
'''

def descending_order(num):
    num_arr = [str(x) for x in str(num)]
    print(type(num_arr))

    num_arr.sort(reverse=True)
    num = ''.join(num_arr)
    print(num)
    return int(num)

descending_order(123456789)