#create a abstract class for the rbi and with methods of rate of intrest and account type methods in abstract class and use them in a sbi,hdfc,canara bank class.

from abc import ABC,abstractmethod
class rbi:
    @abstractmethod
    def rbi_details(self):
        print("rbi")
        pass
    @abstractmethod
    def rate_of_intresr(self,roi):
        print("rate of intrest")
        pass
    @abstractmethod
    def type_of_account(self,toa):
        print("type_of_account")
        pass

class sbi(rbi):
    def __init__(self,bname,baddress):
        self.banme=bname
        self.baddress=baddress

    def sbi_details(self):
        print(self.banme)
        print(self.baddress)

    def rate_of_intresr(self, roi):
        print(roi)
    
    def type_of_account(self,toa):
        print(toa)
        
class canara(rbi):
    def __init__(self,bname,baddress):
        self.banme=bname
        self.baddress=baddress

    def canara_details(self):
        print(self.banme)
        print(self.baddress)

    def rate_of_intresr(self, roi):
        print(roi)
    
    def type_of_account(self,toa):
        print(toa)
class hdfc(rbi):
    def __init__(self,bname,baddress):
        self.banme=bname
        self.baddress=baddress

    def hdfc_details(self):
        print(self.banme)
        print(self.baddress)

    def rate_of_intresr(self, roi):
        print(roi)
    
    def type_of_account(self,toa):
        print(toa)
        

s1=sbi("sbi","vizag")
c1=canara("canara","hyb")
h1=hdfc("hdfc","ttd")
print()
s1.sbi_details()
s1.rate_of_intresr("0.8%")
s1.type_of_account("savings")
print()
c1.canara_details()
c1.rate_of_intresr("11.1%")
c1.type_of_account("current")
print()
h1.hdfc_details()
h1.rate_of_intresr("5.6%")
h1.type_of_account("savings")