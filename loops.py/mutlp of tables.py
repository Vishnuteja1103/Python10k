# multiplication of tables 
#------------ using for loop -------------

num=int(input("enter tables you want up to : "))
for i in range(1,num+1):
    for j in range(1,11):
        print(f"{i} x {j} : {i*j}")
    print()

# -----------using while loop ------------

num = int(input(" enter tables you want up to : "))
i=1
while i<=num:
    for i in range(1,num+1):
        for j in range(1,11):
            print(f"{i} x {j} : {i*j} ")
        print()
    i=i+1
#-------single table -------------
num=int(input("enter a number :"))
for i in range(1,11):
    print(f"{num} x {i} : {num*i}")
