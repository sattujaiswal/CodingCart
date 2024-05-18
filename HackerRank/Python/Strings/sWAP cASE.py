
#method 1 normal logic
def swap_case(s):
    x=""
    for c in s:  #AmaN
        if c.isupper():
            c=c.lower()
        else:
            c=c.upper() 
        x+="".join(c)              
    return x

#method 2 using inbuilt function
def swap_case(s):
    return s.swapcase()

