class employee:
    def __init__(self,name,id,sal):
        self.name=name
        self.id=id
        self.sal=sal

e1=employee("naga",1,20000)
e2=employee("vishnu",2,30000)

# by using functions
employees=[]
def add_details(item):
    # for e in employees:
    employees.append(item)
    print("data added")

def view_details():
    for e in employees:
        print(e.name)
        print(e.id)
        print(e.sal)
    # print(employees)

def update_details(id,new_sal):
    for e in employees:
        if id==e.id:
            e.sal=new_sal
            print("Salary updated")

def delete_details(id):
    for e in employees:
        if id==e.id:
            employees.remove(e1)
        print("deleted")
             
add_details(e1)
add_details(e2)
view_details()
update_details(1,100000)
view_details()
delete_details(1)
view_details()