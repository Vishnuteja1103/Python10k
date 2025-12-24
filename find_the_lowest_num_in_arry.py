values=[5,11,34,3,88,45,1,-3,-1]

minval=values[0]

for i in values:
    if i < minval:
        minval = i
print(f"lowest value in arry : {minval}")