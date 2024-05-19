#method 1
from itertools import permutations
s,k=(input().rsplit())
x=list(permutations(s,int(k)))
l=[''.join(i)for i in x]
l.sort()
for i in l:
    print(i)

#method 2
from itertools import permutations
s=input().split()
string=sorted(s[0])
number=int(s[1])
print(*list(map(''.join,permutations(string,number))),sep='\n')
    #4   3     2                      1                  5