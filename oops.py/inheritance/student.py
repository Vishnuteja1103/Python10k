class student:
    def __init__(self,sname,sage):
        self.sname=sname
        self.sage=sage
    def st_details(self):
        print(self.sname)
        print(self.sage)

class employee(student):
    def __init__(self, sname, sage,ename,eage,edepartment):
        super().__init__(sname, sage)
        self.ename=ename
        self.eage=eage
        self.edepartment=edepartment

    def emp_details(self):
        print("student details :")
        super().st_details()
        print()
        print("employee details :")
        print(self.ename)
        print(self.edepartment)
        print(self.eage)

emp1=employee("vishnu",22,"dinesh vanga",22,"cse")
emp1.emp_details()
