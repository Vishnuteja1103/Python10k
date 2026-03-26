class student:
    def __init__(self,sname,sage):
        self.sname=sname
        self.sage=sage
    def stu_details(self):
        print(self.sname)
        print(self.sage)

class collage(student):
    def __init__(self, sname, sage,cname,cyear):
        super().__init__(sname, sage)
        super().stu_details()
        self.cname=cname
        self.cyear=cyear

    def c_details(self):
        print(self.cname)
        print(self.cyear)

c1=collage("vishnu",22,"raghu",2001)
c1.c_details()