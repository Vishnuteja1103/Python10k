#positive slicing 

s2="hi friends ela unnaru friends"

e1=s2[0:2] #hi
e2=s2[11:14]  #ela
e3=s2[15:21]  #unnaru
e4=s2[3:8:2]   #fin
e5=s2[11:18:3]   #e n
e6=s2[3:16:6]  #fsu
e7=s2[::28]  #hs
print(e1)
print(e2)
print(e3)
print(e4)
print(e5)
print(e6)
print(e7)

e8=s2[::-1] #to print the complete string reverse using postivie slicing index.
e9=s2[-1:-30:-1]  #to print the complete string reverse using negative  slicing index.

print(s2)
print(e8)
print(e9)
