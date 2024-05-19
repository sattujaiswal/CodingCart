n,m=map(int,input().split())
s1='.|.'
s2='WELCOME'
#part1. upper
for i in range(n//2):
    print((s1*((i*2)+1)).center(m,'-'))
#part 2   
print(s2.center(m,'-')) 
#part 3
for i in range(n//2-1,-1,-1):
    print((s1*((i*2)+1)).center(m,'-'))
