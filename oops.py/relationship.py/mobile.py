
class iphone:
    def __init__(self,core,storeage):
        self.core=core
        self.storeage=storeage
    def i13(self):
        print(self.core)
        print(self.storeage)

class oppo:
    def __init__(self,core,storeage):
        self.core=core
        self.storeage=storeage
    def f10pro(self):
        print(self.core)
        print(self.storeage)

class samsung:
    def __init__(self,core,storeage):
        self.core=core
        self.storeage=storeage
    def s24ultra(self):
        print(self.core)
        print(self.storeage)

class mobile:
    def __init__(self,ios,and1,and2):
        self.ios=ios
        self.and1=and1
        self.and2=and2
    
    def mp(self):
        self.ios.i13()
        self.and1.f10pro()
        self.and2.s24ultra()

apple=iphone("a13",234)
o=oppo("opp2",345)
s=samsung("samsung",853)

m=mobile(apple,o,s)
m.mp()




 