class customer:
    def __init__(self,cname,cage):
        self.cname=cname
        self.cage=cage

class bank(customer):
    def __init__(self, cname, cage,balance,mainpin):
        super().__init__(cname, cage,)
        self.balance=balance
        self.mainpin=mainpin
    
    def deposit(self,amount,userpin):
        if userpin==self.mainpin:
            if amount>0:
                self.balance=self.balance+amount
                print(f"amount credited {amount} in your account {self.balance}")
            else:
                print("enter valid amount")
        else:
            print("invalid pin")
    

b1=bank("vishnu",22,5000,1103)
b1.deposit(5000,1103)


