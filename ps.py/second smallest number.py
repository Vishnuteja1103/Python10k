l1=[2,4,1,6,2,4]
smallest=float("inf")
secondsmallest=float("inf")
for i in l1:
    if i < smallest:
        secondsmallest=smallest
        smallest=i
    elif i<secondsmallest and i !=smallest:
        secondsmallest=i

print(secondsmallest)