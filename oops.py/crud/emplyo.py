from abc import ABC,abstractmethod
class person(ABC):
    @abstractmethod
    def insert_details(self):
        pass

    @abstractmethod
    def view_details(self):
        pass

    @abstractmethod
    def update_details(self):
        pass

    @abstractmethod
    def delette_details(self):
        pass

class employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

class employee_management(person):
    details=[]
    def add_details(self,items):
        for i in self.details:
            if i.id==items.id:
                print("DATA EXISTS...")
                return
        self.details.append(items)
        print("DATA INSERTED SUCCESFUULY...")
    
    def view_details(self):
        for i in self.details:
            print(i.id)
            print(i.name)
            print(i.salary)


    def update_details(self,id,**kwargs):
        for i in self.details:
            if i.id==id:
                if 'name' in kwargs:
                    i.name=kwargs['name']
                    print("NAME UPDATED...")
                if 'new_id' in kwargs:
                    i.id=kwargs['new_id']
                    print("ID UPDATED")
                if 'salary' in kwargs:
                    i.salary=kwargs['salary']
                    print("SALARY UPDATED")
            return
        print("INVALID ID")
    
    def delette_details(self,id):
        for i in self.details:
            if i.id==id:
                self.details.remove(i)
                print("DELETD")
                return
        print("INVALID ID")


e=employee(1,"vishnu",289999)
ee=employee(2,"teja",2000000)
e1=employee_management()
e1.add_details(e)
e1.add_details(ee)
e1.view_details()
e1.update_details(1,salary=5000)
e1.view_details()
e1.delette_details(2)
e1.view_details()