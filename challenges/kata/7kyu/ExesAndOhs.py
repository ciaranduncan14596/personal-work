'''
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

'''

def xo(s):
    xo_dict = {
        'x': 0,
        'o': 0,
    }
    xo_arr = [ char for char in s]
    for char in xo_arr:
        if char.lower() == 'x': 
            xo_dict['x'] = xo_dict['x'] + 1
        if char.lower() == 'o':
            xo_dict['o'] = xo_dict['o'] + 1
    if xo_dict['x'] == xo_dict['o']:
        return True
    return False

a = xo('xo')
print(a)