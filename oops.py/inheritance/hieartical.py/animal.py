class animal:
    def __init__(self,legs,sounds):
        self.legs=legs
        self.sounds=sounds
    def animal_details(self):
        print(self.legs)
        print(self.sounds)

class cat(animal):
    def __init__(self, legs, sounds,cat_name,cat_sound):
        super().__init__(legs, sounds)
        self.cat_name=cat_name
        self.cat_sound=cat_sound

    def cat_details(self):
        super().animal_details()
        print(self.cat_name)
        print(self.cat_sound)

class dog(animal):
    def __init__(self, legs, sounds,dog_name,dog_sound):
        super().__init__(legs, sounds)
        self.dog_name=dog_name
        self.dog_sound=dog_name

    def dog_details(self):
        super().animal_details()
        print(self.dog_name)
        print(self.dog_sound)

class leapord(animal):
    def __init__(self, legs, sounds,leapord_name,leapord_sound):
        super().__init__(legs, sounds)
        self.leapord_name=leapord_name
        self.leapord_sound=leapord_sound

    def leapord_details(self):
        super().animal_details()
        print(self.leapord_name)
        print(self.leapord_sound)

c1=cat(4,"sound","shii","mewo")
c1.cat_details()
print()

d1=dog(4,"sound","dora","boo-boo")
d1.dog_details()
print()

l1=leapord(4,"sound","chotu","gruu-gruuu",)
l1.leapord_details()
print()