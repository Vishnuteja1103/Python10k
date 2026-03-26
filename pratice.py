# s=str(input("enter a string:"))
# s1=s[0:2]
# s2=s[-2:]
# s3=s1+s2
# print(s3)

# a="python"
# s1=a[3:10]
# print(s1)

lst=[1,2,3,4,5]
temp=lst[0]
lst[0]=lst[-1]
lst[-1]=temp
print(lst)

#print half of the list 
# a =[1,2,3,4,5,6]
# b=len(a)
# c=b//2
# e=a[c:]
# print(e)

# l=list(map(int,input().split()))
# n=len(l)
# x=n//2
# print(l[x:])