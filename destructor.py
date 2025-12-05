class Product :
    def __init__ (self,qty,price):
        self.total=qty * price
        print("total=",self.total)
    def __del__ (self):
        print("destructor called")
obj1=Product(10,500)
obj2=Product(12,500)
obj3=Product(15,500)