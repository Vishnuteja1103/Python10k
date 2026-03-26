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


class student:
    def __init__(self,name,id,marks):
        self.name=name
        self.id=id
        self.marks=marks

class student_managemnt(person):
    details=[]
    def insert_details(self,items):
        for i in self.details:
            if i.id==items.id:
                print("data already exits")
                return 
        self.details.append(items)
        print("data added successfully")

    def view_details(self):
        for i in self.details:
            print(i.name)
            print(i.id)
            print(i.marks)

    def update_details(self,id,**kwargs):
        for i in self.details:
            if i.id==id:
                if 'name' in kwargs:
                    i.name=kwargs['name']
                    print("name update..")
                if 'id' in kwargs:
                    i.id=kwargs['id']
                    print("id update")
                if "marks" in kwargs:
                    i.marks=kwargs['marks']
                    print("marks update ")
            return
        print("invalid id")

    def delette_details(self,id):
        for i in self.details:
            if i.id==id:
                self.details.remove(i)
                print("deleted")
                return
        print("invalid id")

st1=student("vishnu",2,87)
st2=student("teja",3,95)

s1=student_managemnt()
s1.insert_details(st1)
s1.insert_details(st2)
s1.view_details()
s1.update_details(2,marks=100)
s1.view_details()
s1.delette_details(2)
s1.view_details()
