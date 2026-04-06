n=5
for i in range(1,n+1):
    num = 1 if i%2!=0 else 0

    for j in range(i):
        print(num,end=" ")
        num=1-num
    print()
 