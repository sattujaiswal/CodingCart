
from itertools import combinations
n=int(input())
l=list(input().split())
k=int(input())
c=list(combinations(l,k))
r=[i for i in c  if 'a' in i]
print('%.3f'%(len(r)/len(c)))


#taking 3 variables in single line
from itertools import combinations
n,s,r = int(input()),input().split(),int(input())
t = list(combinations(s,r))
f = [i for i in t if 'a' in i]   
print('%.3f'%(len(f)/len(t)))

