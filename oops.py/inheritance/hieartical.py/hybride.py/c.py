class a:
    def a_method(self):
        print("a details")
class b(a):
    def b_method(self):
        print("b details")

class c(a):
    def c_method(self):
        print("c details")

class d(b,c):
    def d_method(self):
        print("d details")

d1=d()
c1=c()
c1.a_method()
d1.b_method()
d1.c_method()
