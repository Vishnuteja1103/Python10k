class a:
    def a_details(self):
        print("a details")

class b:
    def b_details(self):
        print("b details")

class c(a,b):
    def c_details(self):
        print("c details")

class d(a,b):
    def d_details(self):
        print("d details")

class e(a,b):
    def e_details(self):
        print("e details")

class f(c,d,e):
    def f_details(self):
        print("f details")

f1=f()
e1=e()
d1=d()
c1=c()

f1.a_details()
f1.b_details()
f1.c_details()
f1.d_details()
f1.e_details()
f1.f_details()
