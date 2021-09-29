'''
Given a string of digits,
 you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
  Return the resulting string.
'''

def fake_bin(x):
    int_arr = [int(i) for i in x]
    new_str =''
    for i in int_arr:
        if i <5:
            new_str = new_str + '0'
        else:
            new_str = new_str + '1'
    return new_str

a = fake_bin('1234556546')
print(a)
