class SBI:
    def __init__(self,sname,spincode):
        self.sname=sname
        self.spincode=spincode
    def smethod(self):
        print()
        print("SBI")
        print(self.sname)
        print(self.spincode)

class HDFC:
    def __init__(self,hname,hpincode):
        self.hname=hname
        self.hpincode=hpincode

    def hmethod(self):
        print()
        print("HDFC")
        print(self.hname)
        print(self.hpincode)

class union:
    def __init__(self,uname,upincode):
        self.uname=uname
        self.upincode=upincode

    def umethod(self):
        print()
        print("union")
        print(self.uname)
        print(self.upincode)

class RBI:
    def __init__(self,sbi_d,hdfc_d,union_d):
        self.sbi_d=sbi_d
        self.hdfc_d=hdfc_d
        self.union_d=union_d
    def rbi_details(self):
        self.sbi_d.smethod()
        self.hdfc_d.hmethod()
        self.union_d.umethod()   

s1=SBI("sbi",1234)
h1=HDFC("HDFC",34567)
u1=union("union",4535)

r1=RBI(s1,h1,u1)
r1.rbi_details()
