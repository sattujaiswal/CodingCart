from collections import Counter
n=int(input())
l=list(map(int, input().split()))
x=int(input())
l1=dict(Counter(l))
s=0
for _ in range(x):
    a,b=map(int, input().split())
    if a in l1.keys() and l1[a]>0:
        s+=b
      #  print('1st',l1[a])
        l1[a]-=1
        #print('2nd',l1[a])  
print(s)