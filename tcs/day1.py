# square patterns 
n=3
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

n=3
for i in range(n):
    for j in range(n):
        print(j+1,end=" ")
    print()

n=3
for i in range(n):
    for j in range(n):
        print(i+1,end=" ")
    print()

n=3
for i in range(n):
    num=97
    for j in range(n):
        print(chr(num),end=" ")
        num+=1
    print()


n=3
num=97
for i in range(n):
    for j in range(n):
        print(chr(num),end=" ")
        num+=1
    print()
# a b c 
# d e f 
# g h i

n=3
num=97
for i in range(n):
    for j in range(n):
        print(chr(num),end=" ")
        # num+=1
    print()

n=3
num=97
for i in range(n):
    for j in range(n):
        print(chr(num),end=" ")
    print()
    num+=1


for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(5):
    for j in range(i):
        print(" *",end=" ")
    print()

  