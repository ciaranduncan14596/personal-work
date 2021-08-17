'''
https://www.codewars.com/kata/5270d0d18625160ada0000e4/python
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, 
is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll. For example, a given "5" 
can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
'''

def greed(array):
    dict_of_num = {}
    for number in array:
        if number not in dict_of_num:
            dict_of_num[number] = 1
        else:
            dict_of_num[number] = dict_of_num[number] + 1
    total = 0
    for i in range(1, 7):
        if i in dict_of_num.keys():
            num = dict_of_num[i]
            while num !=0:
                if i == 1 and num >= 3:
                    total += 1000
                    num = num - 3
                elif num >= 3:
                    total = total + (i *100)
                    num = num -3
                elif i == 1 and num < 3:
                    total += 100
                    num = num -1
                elif i == 5 and num < 3:
                    total += 50
                    num = num -1
                else:
                    num = num -1
    return total
            


# greed([1, 1, 1, 3, 1])
a = greed([1,1,1,6,2])
print(a)