class cse:
    def __init__(self,dname,did):
        self.dname=dname
        self.did=did
    def c1(self):
        print()
        print(self.dname)
        print(self.did)

class ece:
    def __init__(self,ename,eid):
        self.ename=ename
        self.eid=eid
    
    def e1(self):
        print()
        print(self.ename)
        print(self.eid)

class meh:
    def __init__(self,mname,mid):
        self.mname=mname
        self.mid=mid
    
    def m1(self):
        print()
        print(self.mname)
        print(self.mid)

class collage:
    def __init__(self,cse_1,ece_1,meh_1):
        self.cse_1=cse_1
        self.ece_1=ece_1
        self.meh_1=meh_1
    def collage_d(self):
        self.cse_1.c1()
        self.ece_1.e1()
        self.meh_1.m1()

c11=cse("computer science","c202")
e11=ece("electronic","e34")
m11=meh("mehical","m3256")

co=collage(c11,e11,m11)
co.collage_d()
        
