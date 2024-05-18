n=int(input())
student={}
for i in range(n):
    name, *marks=input().split()  #'amit 56 78 90'  -->'amit' '56' '78' '90'
   # print(name)
   # print(marks)
    marks=list(map(float,marks))
  #  print(marks)
    student[name]=marks
qname=input()   
score=student[qname]  #list of marks   [56,78,90]
#print(score)

#format(val,'.nf')
print(format(sum(score)/3,'.2f'))
