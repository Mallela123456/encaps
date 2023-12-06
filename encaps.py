#public: we can access anyhwhere in the class
# class A:
#     number = 100 
#     def public(self):
#         print(self.number)
# class C(A):
#     def show(self):
#         print(self.number)
# obj1 = A()
# obj1.public()
# print(obj1.number)
# obj2 = C()
# obj2.show()        
# print(obj2.number)

#private:it can only access in that class
# class A:
#     __number = 200 
#     def private(self):
#         print(self.__number)
# class C(A):
#     def show(self):
#         print(self.__number)
# obj1 = A()
# obj1.private()

#protect:it can access only that class & child class
class A:
    _number = 200 
    def private(self):
        print(self._number)
class C(A):
    def show(self):
        print(self._number)
obj1 = A()
obj1.private()
obj2 = C()
obj2.show()



            
