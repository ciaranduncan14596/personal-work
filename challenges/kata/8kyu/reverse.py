def solution(string):
    new_string = ''
    s = [ char for char in string]
    for i in range(0, len(s)):
        new_string += s[len(s)-1 -i ]


solution('world')