# def sumn(i,sum):
#     if i<1: 
#         print(sum)
#         return
#     else:
#         sumn(i-1,sum+i)
#         return

# sumn(3,0)

def sumn(a):
    if a==0:
        return 0
    else:
        return a + sumn(a-1)

print(sumn(3))