'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''

def domain_name(string):
    string_array = string.replace('http://', '').replace('https://','').split('/')
    for string in string_array:
        if string[:3] in ['www']:
            return string.split('.')[1]
        return string.split('.')[0]

a = domain_name("http://github.com/carbonfive/raygun")
b = domain_name("http://www.zombie-bites.com")
c = domain_name("http://google.co.jp")

print(a,b,c)