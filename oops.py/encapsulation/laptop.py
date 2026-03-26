class laptop:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price

    def lap_details(self):
        print(self.name)
        print(self.model)
        print(self.price)

    def set_method(self,deal_price):
        if deal_price>self.price:
            print("deal okay sweety 😎😎")
        else:
            print("deal not okay sweety 😢😢 to cheap you are 😌")

lp=laptop("dell","i5",68000)
lp.lap_details()
print()
lp.set_method(70000)
print()
print(lp.price)
print(lp.model)
print(lp.price)


