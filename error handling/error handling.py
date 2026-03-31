#handle the key error
try:
    a1={'1':'a','2':'b'}
    print(a1['3'])
except KeyError as msg:
    print("KeyError:" ,msg)

#handle the multiple errors



try:
   a=int(input("Enter value1: "))
   b=int(input("Enter value2: "))
   print(a/b)
except ZeroDivisionError as msg:
    print(msg)
except ValueError as msg:
    print(msg)

try:
   a=int(input("Enter value1: "))
   b=int(input("Enter value2: "))
   print(a/b)
except (ZeroDivisionError,ValueError) as msg:
    print(msg)

#***********************************************************************************************************************
#kabaddi selection[age,height,weight]
class KabaddiException(Exception):
    pass
try:
    age=int(input("Enter age: "))
    height=int(input("Enter height:"))
    weight=int(input("Enter weight: "))
    if(age>=18 and height>=170 and weight>=60 or weight<=70):
        print("Eligible for playing kabaddi")
    if(age<18):
        raise KabaddiException("Not eligible as age is less")
    if(height<170):
        raise KabaddiException("Not Eligible as height is less than requirement")
    if(weight<60 or weight>70):
        raise KabaddiException("Not Eligible as weight is less than requirement")
except KabaddiException as msg:
    print(msg)

#placmentselections

class PlacementException(Exception):
    pass
try:
    degree=(input("Enter degree: "))
    branch=(input("Enter branch:"))
    level=(input("Enter level : "))
    if(branch=='IT' or branch=='CSE' or branch=='CSSE' and degree=='B.Tech' and level=='l3'):
        print("Eligible for Placement")
    if(branch!='IT' or branch!='CSE' or branch!='CSSE'):
        raise PlacementException("Not eligible as branch is not per requirement")
    if(degree!='B.Tech' ):
        raise PlacementException("Not Eligible as  degree is not per requirement")
    if(level!='l3'):
        raise PlacementException("Not Eligible as  level is not per requirementt")
except PlacementException as msg:
    print(msg)