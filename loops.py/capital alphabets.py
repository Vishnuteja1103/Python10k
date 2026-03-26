# print the capital letters

for i in range(65,91):
    print(chr(i))

# print lower letters 

for i in range(97,123):
    print(chr(i))


#------------------------------------------------------
#---------samll letters ------------
l=[]
for i in range (97,123):
    
    # l.append(chr(i))
    l+=[chr(i)]

print(l)
for j in l:
    print(ord(j))
   
#----------------capital letters----------------------

l=[]
for i in range (65,91):
    
    # l.append(chr(i))
    l+=[chr(i)]

print(l)
for j in l:
    print(ord(j))
   



