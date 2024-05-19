#method 1
def print_full_name(a, b):
    print("Hello "+a+" "+b+"! "+"You just delved into python.")

#method 2
def print_full_name(a, b):
    #print("Hello "+a+" "+b+"! "+"You just delved into python.")
    print("Hello {1} {0}! You just delved into python. ".format(b,a))
