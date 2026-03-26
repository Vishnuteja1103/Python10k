l1=[2,6,1,8,97,53,12,1,1,53,97]
largest=0
secondl=0
for i in l1:
    if i>largest:
        largest=i

for j in l1:
    if j>secondl and j<largest:
        secondl=j

print("largest:",largest)
print("second largest:",secondl)

