class windows5:
    def __init__(self,wname,wyear):
        self.wname=wname
        self.wyear=wyear

    def w5method(self):
        print(self.wname)
        print(self.wyear)

class windows6(windows5):
    def __init__(self, wname, wyear,w6name,w6year):
        super().__init__(wname, wyear)
        super().w5method()
        self.w6name=w6name
        self.w6year=w6year

    def w6_details(self):
        print()