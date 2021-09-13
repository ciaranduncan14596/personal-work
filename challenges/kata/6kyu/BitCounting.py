'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 
You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''

def count_bits(integer):
    a = bin(integer)
    list_a = [ letter for letter in a ]
    counter = 0
    for letter in list_a:
        if letter == '1':
            counter += 1
    
    return counter

a = to_bin(1234)
print(a)