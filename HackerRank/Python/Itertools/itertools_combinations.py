#method 1
from itertools import combinations
s=input().split()
string=sorted(s[0])
number=int(s[1])
for i in range(1,number+1):
    x=list(combinations(string,i))
    for val in x:
        print(''.join(val))


#method 2
from itertools import combinations
s=input().split()
string=sorted(s[0])
number=int(s[1])
for i in range(1,number+1):
    print(*list(map(''.join,combinations(string,i))),sep='\n')        
