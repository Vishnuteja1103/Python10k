class student:
    collagename="american express bank"
    def __init__(self,name,account_type,credit_card):
        self.name=name
        self.account_type=account_type
        self.credit_card=credit_card
    def method(self):
        print(self.collagename,self.name,self.account_type,self.credit_card)
        
 
s1=student("vishnu","savings","yes")
s2=student("dinesh","savings","no")
s3=student("charan","savings","yes")
s4=student("vamsi","savings","no")
s5=student("ram","savings","yes")

s1.method()
s2.method()
s3.method()
s4.method()
s5.method()

