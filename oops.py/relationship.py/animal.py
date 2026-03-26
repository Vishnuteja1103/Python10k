class animal:
    def __init__(self,sound):
        self.sound=sound
    def sound1(self):
        print(self.sound)

class dog:
    def __init__(self,name,born):
        self.name=name
        self.born=born
    def dog1(self):
        animal("boo b00").sound1()
        print(self.name)
        print(self.born)

class cat:
    def __init__(self,name,born):
        self.name=name
        self.born=born
    def cat1(self):
        animal("meow meow").sound1()
        print(self.name)
        print(self.born)

class snake:
    def __init__(self,name,born):
        self.name=name
        self.born=born
    def snake1(self):
        animal("bushhhhhh").sound1()
        print(self.name)
        print(self.born)


b=dog("bora",2015)
b.dog1()
print()
c=cat("shoo",2019)
c.cat1()
print()
s=snake("nag",2006)
s.snake1()