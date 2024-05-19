
#method 1 using inbuilt string function
import string 
def solve(s):
    return string.capwords(s, ' ')




#method 2
def solve(s):
     return ' '.join(i.capitalize() for i in s.split(' '))



