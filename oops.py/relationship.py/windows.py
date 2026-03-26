# #create window 9 class,windows 10 class,windows 11 class and create relation inside microsoft class
class window9:
    def __init__(self,core,storeage):
        self.core=core
        self.storeage=storeage
    def w9(self):
        print(self.core)
        print(self.storeage)

class window10:
    def __init__(self,core,storeage):
        self.core=core
        self.storeage=storeage
    def w10(self):
        print(self.core)
        print(self.storeage)

class window11:
    def __init__(self,core,storeage):
        self.core=core
        self.storeage=storeage
    def w11(self):
        print(self.core)
        print(self.storeage)

class microsoft:
    def __init__(self,v9,v10,v11):
        self.v9=v9
        self.v10=v10
        self.v11=v11
    
    def mc(self):
        self.v9.w9()
        self.v10.w10()
        self.v11.w11()

vv9=window9("i5",256)
vv10=window10("i6",556)
vv11=window11("i7",1080)

mmcc=microsoft(vv9,vv10,vv11)
mmcc.mc()