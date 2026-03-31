# print vowels in the file 
f=open("file.txt","r")
for i in f.read():
    if i in "aeiouAEIOU":
        print(i)
f.close()

#  print only digit in the file 
f=open("file.txt","r")
d=[]
for i in f.read():
    if i in "0123456789":
        d.append(i)
print(d)
f.close

# convert all the character into upper case:
f=open("file.txt","r")
d=[]
for i in f.read():
    print(i.upper(),end="")
    d.append(i.upper())
print(d)
f.close
#  convert all the character into lower case:
f=open("file.txt","r")
d=[]
for i in f.read():
    print(i.lower(),end="")
    # d.append(i.lower())
print(d)
f.close
# count the charactre in the file 
f=open("file.txt","r")
count=0
for i in f.read():
    count+=1
print(count)
f.close
#  sum of all asic values in the file 
f=open("file.txt","r")
sum=0
for i in f.read():
    sum=sum+ord(i)
print(sum)
f.close

# remove the spaces from the file
f=open("file.txt","r")
for i in f.read():
    if i !=" ":
        print(i,end="")
f.close
