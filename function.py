
# class product:
#     def setvalue(self):
#         self.code=int (input ("Enter product code : "))
#         self.name=(input ("Enter product name : "))
#     def display(self):
#         print("code=",self.code)
#         print("name=",self.name)
# obj=product()
# print(type(obj))
# obj.setvalue()
# obj.display()




class product:
    def setvalue(self,x,y):
        self.code=x
        self.name=y
    def display(self):
        print("code=",self.code)
        print("name=",self.name)
obj=product()
print(type(obj))
obj.setvalue(101,"Motorola-")
obj.display()


