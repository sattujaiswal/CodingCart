
#method 1
from collections import namedtuple
n=int(input())
student=namedtuple('student',input())
lst=[]
s=0
for i in range(n):
    x=input().split()
    s1=student(*x)
    lst.append(s1)
# print(student) #student class name
# print(s1)  #detail of last student
# print(lst)

#cal avg
for i in range(n):
    s+=int(lst[i].MARKS)
print(s/n)    


 
 #method 2
from collections import namedtuple
n=int(input())
student=namedtuple('student',input())
print(sum([  int(student(*input().split()).MARKS)    for i in range(n)])/n)