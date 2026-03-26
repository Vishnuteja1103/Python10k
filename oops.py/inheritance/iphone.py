class iphone14:
    def __init__(self,model,camera):
        self.model=model
        self.camera=camera
    
    def i14_details(self):
        print(self.model)
        print(self.camera)
        print()

class iphone15(iphone14):
    def __init__(self, model, camera,i15model,i15camera):
        super().__init__(model, camera)
        super().i14_details()
        self.i15model=i15model
        self.i15camera=i15camera

    def i15_details(self):
        # super().i14_details()
        print(self.i15model)
        print(self.i15camera)

class iphone16(iphone15):
    def __init__(self, model, camera, i15model, i15camera,i16model,i16camera):
        super().__init__(model, camera, i15model, i15camera)
        super().i15_details()
        self.i16model=i16model
        self.i16camera=i16camera

    def i16_details(self):
        # super().i14_details()
        
        print(self.i16camera)
        print(self.i16model)

a16=iphone16("14","12","15","14","16","48")
a16.i14_details()