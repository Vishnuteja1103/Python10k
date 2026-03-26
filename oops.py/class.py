class student:
    name="vishnu"
    age=22
    id=11
    def method1(self):
        print(self.name)
        print(self.id)
        print(self.age)
        print("anime")
        print("sports")


stu=student()

stu.method1()




# -------------------------------------------------------------


class bike:
    name="java 42"
    price=300000
    model=42
    brand="apple"
    modelp="14"
    gb="128"
    def vbike(self):
        print(self.name)
        print(self.price)
        print(self.model)
    def vphone(self):
        print(self.brand)
        print(self.modelp)
        print(self.gb)

s=bike()
s.vbike()
s.vphone()
print(s.brand)



class mobile:
    brand="apple"
    mobel="14"
    color="mid night blue"
    chip="a13"
    display="oled"
    def method1(v):
        print(v.brand)
        print(v.chip)
        print(v.color)
        print(v.display)
        # print(v.method1)
    def method2(i):
        print("capcut")
        print("hypic")
        print("youtube")
    def method3(s):
        print("music")
        print("video")
        print("games")

v1=mobile()
v1.method1()
v1.method2()
v1.method3()
print(v1.brand)