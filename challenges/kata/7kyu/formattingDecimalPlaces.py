'''
Each floating-point number should be formatted that only the first two decimal places are returned. You don't need to check whether the input is a valid number because only valid numbers are used in the tests.

Don't round the numbers! Just cut them after two decimal places!

Right examples:  
32.8493 is 32.84  
14.3286 is 14.32

Incorrect examples (e.g. if you round the numbers):  
32.8493 is 32.85  
'''

def two_decimal_places(number):
    number_str = str(number)

    split = number_str.split('.')
    after_dp = split[1][0:2]

    return float(split[0]+ "." + after_dp)

x = two_decimal_places(32.8493)
print(x)