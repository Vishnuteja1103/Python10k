from abc import ABC,abstractmethod
class inventory(ABC):
    @abstractmethod
    def add_products(self):
        pass

    @abstractmethod
    def view_products(self):
        pass

    @abstractmethod
    def update_products(self):
        pass

    @abstractmethod
    def delete_products(self):
        pass

    @abstractmethod
    def total(self):
        pass

class products:
    def __init__(self,name,id,price,quantity):
        self.name=name
        self.id=id
        self.quantity=quantity
        self.price=price


class inventory_management(inventory):
    details=[]
    total_price=0
    def add_products(self,items):
        for i in self.details:
            if i.id==items.id:
                print("item with same id already exists..")
                return
        self.details.append(items)
        print("PRODUCTS ADDED SUCCESFULLY")

    def view_products(self):
        for i in self.details:
            print(i.id)
            print(i.name)
            print(i.quantity) 
            print(i.price)
            print()

    def update_products(self,id,**kwargs):
        for i in self.details:
            if id==id:
                # if 'name' in kwargs:
                #     i.name=kwargs['name']
                #     print("name updated")
                # if 'new_id' in kwargs:
                #     i.id=kwargs['new_id']
                #     print("id updated")
                if 'price' in kwargs:
                    i.price=kwargs['new_price']
                    print("price updated")
                if 'quantity' in kwargs:
                    i.quantity=kwargs['quantity']
                    print("quantity updated")
                return
            print("id not found")

    def delete_products(self):
        for i in self.details:
            if i.id==id:
                self.details.remove(i)
                print("product deleted")
                return
        print("invalid id ")

    def total(self):
        for i in self.details:
            self.total_price=i.price*i.quantity
        print(self.total_price)

p1=products("sunscreen",123,560,3)
p2=products("facewash",567,280,2)

pm1=inventory_management()
pm1.add_products(p1)
pm1.add_products(p2)


# pm1.view_products()
pm1.update_products(5,quantity=4)
pm1.view_products()

pm1.total()