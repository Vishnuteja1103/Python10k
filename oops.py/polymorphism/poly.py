# create  aclass for the vehicle and create method for engine  and create classes for the car,bike,truck and achive the overiding 
# class vehicle :
#     def __init__(self,vehicleno,model):
#         self.vehicleno=vehicleno
#         self.model=model
#     def engine(self):
#         print(self.vehicleno)
#         print(self.model)
# class bike(vehicle):
#     def __init__(self,bname,bmodel):
#         self.bname=bname
#         self.bmodel=bmodel
#     def engine(self):
#         print(self.bname)
#         print(self.bmodel)

# class car(vehicle):
#     def __init__(self,cname,cmodel):
#         self.cname=cname
#         self.cmodel=cmodel
#     def engine(self):
#         print(self.cname)
#         print(self.cmodel)
# class truck(vehicle):
#     def __init__(self,tname,tmodel):
#         self.tname=tname
#         self.tmodel=tmodel
#     def engine(self):
#         print(self.tname)
#         print(self.tmodel)

# v1=vehicle("engine","300cc")
# v1.engine()
# b1=bike("jawa",42)
# b1.engine()
# c1=car("toyota",2015)
# c1.engine()
# t1=truck("mahindra","model456")
# t1.engine()
#create class for the bank rbi and with method names rate of interst and tge
#  type of account  and create a classes for sbi,hdfc,canara banks and achive overiding.
class RBIbank:
    def __init__(self,type_of_account,rate_of_intrest):
        self.rate_of_intrest=rate_of_intrest
        self.type_of_account=type_of_account
    def rbidetails(self,type_of_account):
        print(type_of_account)
    def rbidetails(selef,rate_of_intrest):
        print(rate_of_intrest)
class sbi(RBIbank):
    def __init__(self, type_of_account, rate_of_intrest):
        def sbi_deatils(self):
            print("sbi bank")
            print("sbi Id:1234")
class hdf(RBIbank):
    def __init__(self, type_of_account, rate_of_intrest):
        def hdfc_deatils(self):
            print("hdfc bank")
            print("hdfc Id:1234")
class carana(RBIbank):
    def __init__(self, type_of_account, rate_of_intrest):
        def carana_deatils(self):
            print("carana bank")
            print("carana Id:12684")
s1=sbi("savings","0.6%")
s1.rbidetails("0.12%")

c1=carana("personal","0.5%")
c1.rbidetails("0.3%")


