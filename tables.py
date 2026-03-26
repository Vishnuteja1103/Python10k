# Python Program to print table of a number
n = int(input("enter a number:"))

def printTable(n):

for i in range (1, 11): 
        
        # multiples from 1 to 10
        # print ("%d * %d = %d" % (n, i, n * i))
    print(f"{n} * {i} = {n*i}")
 

# printTable(n)


# num1 =int(input("enter a num :"))
# num2 =  int(input("enter a num :"))
# opertor = input("enter the opertor :")

# if opertor == "*":
#     print( "multi of two num:", num1 * num2)
# elif opertor =="+":
#     print("adition of two num:",num1 + num2)
# elif opertor == "-":
#     print("sub of two num :",num1 - num2)
# elif opertor == "/":
#     print("division of two num:", num1 / num2)
# else:
#     print("""invalid operator
#           please enter a valid opearator""")



# s1={1,2,3,4}
# s2={2,3,5,6}
# s4={2,3,4,5,8}
# s3=s1.symmetric_difference((s2.symmetric_difference(s4)))
# # print(s3)
# # s3=s1^s2^s4
# print(s3)