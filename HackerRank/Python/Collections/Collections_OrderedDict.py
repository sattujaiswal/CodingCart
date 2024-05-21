##--------try all these below codes ------------##

# from collections import OrderedDict
# od=OrderedDict()
# for i in range(int(input())):
#     str=input().split()
#     k=' '.join(str[:-1])
#     v=int(str[-1])
#     if k in od:
#         od[k]=od[k]+v
#     else:    
#         od[k]=v
# for key,val in od.items():
#     print(key,val)



from collections import OrderedDict
od=OrderedDict()
for i in range(int(input())):
    k,v=input().rsplit(' ',1)
    if k in od:
        od[k]=int(od[k])+int(v)
    else:    
        od[k]=v
for key,val in od.items():
    print(key,val)


# od=dict()
# for i in range(int(input())):
#     k,v=input().rsplit(' ',1)
#     if k in od:
#         od[k]=int(od[k])+int(v)
#     else:
#         od[k]=v    
# for k,v in od.items():
#     print(k,v)

