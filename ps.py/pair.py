l1=[1,2,3,4,5,6,7,8]
target=6
l=[]
for i in l1:
    for j in l1:
        if i + j == target :
            if [i,j] and [j,i] not in l:
                l.append([i,j])
print(l)