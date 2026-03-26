class collage:
    def __init__(self,collagename,place):
        self.collagename=collagename
        self.place=place
    
    def collage_details(self):
        print(self.collagename)
        print(self.place)

class cse(collage):
    def __init__(self, collagename, place,department_name,department_id):
        super().__init__(collagename, place)
        self.department_name=department_name
        self.department_id=department_id

    def cse_details(self):
        super().collage_details()
        print(self.department_name)
        print(self.department_id)

class ece(collage):
    def __init__(self, collagename, place,department_name,department_id):
        super().__init__(collagename, place)
        self.department_name=department_name
        self.department_id=department_id

    def ece_details(self):
        super().collage_details()
        print(self.department_name)
        print(self.department_id)


class meh(collage):
    def __init__(self, collagename, place,department_name,department_id):
        super().__init__(collagename, place)
        self.department_name=department_name
        self.department_id=department_id

    def meh_details(self):
        super().collage_details()
        print(self.department_name)
        print(self.department_id)

c1=cse("raghu","vsp","cse","c01")
c1.cse_details()
print()

e1=ece("raghu","vsp","ece","e02")
e1.ece_details()
print()

m1=meh("raghu","vsp","meh","m03")
m1.meh_details()
print()

