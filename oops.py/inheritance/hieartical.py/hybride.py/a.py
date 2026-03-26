class a:
    def a_method(self):
        print("a details")
class b:
    def b_method(self):
        print("b details")
    
class c(a,b):
    def c_method(self):
        print("c details ")

class d(c):
    def d_method(self):
        print("d details")

c1=c()
c1.c_method()
c1.a_method()
c1.b_method()
d1=d()
d1.d_method()
d1.c_method()
d1.a_method()