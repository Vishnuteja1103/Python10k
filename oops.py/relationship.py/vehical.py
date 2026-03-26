class vehical:
    def __init__(self,engine):
        self.engine=engine

    def engine_method(self):
        print(self.engine)


class bike:
    def __init__(self,name,year):
        self.name=name
        self.year=year

    def method1(self):
        vehical("v4").engine_method()
        print(self.name)
        print(self.year)

# b1=bike()
# b1.method1()


class car:
    def __init__(self,carname,model):
        self.carname=carname
        self.model=model

    def method2(self):
        vehical("v6").engine_method()
        print(self.carname)
        print(self.model)

# c1=car()
# c1.method2()

class truck:
    def __init__(self,truckname,truckmodel):
        self.truckname=truckname
        self.truckmodel=truckmodel

    def method3(self):
        vehical("v8").engine_method()
        print(self.truckname)
        print(self.truckmodel)



b1=bike("java",2025)
b1.method1()

c1=car("bwm","250d")
c1.method2()

t1=truck("lamdorandi","234")
t1.method3()

