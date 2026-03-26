from abc  import ABC,abstractmethod
class collage:
    @abstractmethod
    def collagename(self,cname):
        pass
    
    @abstractmethod
    def collageid(self,cid):
        pass


class cse(collage):
    def __init__(self,branch,section):
        self.branch=branch
        self.section=section

    def cse_details(self):
        print(self.branch)
        print(self.section)

    def collagename(self, cname):
        print(cname)

    def collageid(self, cid):
        print(cid)


class ece(collage):
    def __init__(self,branch,section):
        self.branch=branch
        self.section=section

    def ece_details(self):
        print(self.branch)
        print(self.section)

    def collagename(self, cname):
        print(cname)

    def collageid(self, cid):
        print(cid)

class meh(collage):
    def __init__(self,branch,section):
        self.branch=branch
        self.section=section

    def meh_details(self):
        print(self.branch)
        print(self.section)
        
    def collagename(self, cname):
        print(cname)

    def collageid(self, cid):
        print(cid)
c1=cse("computer science","b")
e1=ece("ece","c")
m1=meh("meh","a")

c1.collageid("r2025")
c1.collagename("raghu")
c1.cse_details()
print()
e1.collageid("r2025")
e1.collagename("raghu")
e1.ece_details()
print()
m1.collageid("r2025")
m1.collagename("raghu")
m1.meh_details()
print()