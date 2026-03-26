#count the frequency of lowercase characters in a string

str=input("enter a string:")
lis=[]
dic={}
for i in str:
    if (ord(i)>=95 and ord(i)<=122):
        lis.append(i)
for j in lis:
    if j in dic:
        dic[j]+=1
    else:
        dic[j]=1
# print(lis)
print(dic)







































 


 