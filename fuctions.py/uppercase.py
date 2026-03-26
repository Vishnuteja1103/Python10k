l1=["vishnu","charan","dinesh","jay","sweety","rohit"]  
res=list(map(lambda a : a.upper(),l1))
res1=list(map(lambda a :len(a),l1))

print(res)
print(res1)

l2=[1,2,3,-1,-5,-4,11,-23]
res2=list(map(lambda a : a+5 if a>0 else a,l2 ))

print(res2)
l3=[1,2,3]
l4=[8,9,7]

res3=list(map(lambda x,y : x+y,l3,l4))
print(res3)




