# class Computer:
#     def __init__(self) -> None:
#         self.__price = 9000

#     def sell(self):
#         print("Selling price :{}".format(self.__price))

#     def setMaxPrice(self, price):
#         self.__maxprice = price


# obj = Computer()
# obj.sell()

# obj.__maxprice = 1000
# obj.sell()

# obj.setMaxPrice(2000)
# obj.sell()
##########################################
# Encapsulation public member             #
##########################################

# class Pub_Mod:
#     def __init__(self,name,age) -> None:
#          self.name = name
#          self.age = age


#     def Age(self):
#         print(self.age)

# obj = Pub_Mod("vivek",20)
# print(obj.name)
# obj.Age()


# Encapsulation private memeber

# class Rectagle:
#     __length = 0
#     __breadth = 0

#     def __init__(self) -> None:
#         self.__length= 20
#         self.__breadth = 40

#         print(self.__length)
#         print(self.__length)

# obj = Rectagle()
# print(obj.length)
# print(obj.breadth)


# Encapsulation protectd member

# class Protected_mem:
#     _name = 'vivek'
#     _age = 20
#     _job = 'python developer'
#     def __init__(self) -> None:
#         print("parant class this.")

# class Pchild(Protected_mem):
#     def __init__(self) -> None:
#         super().__init__()
#         print(self._name)
#         print(self._age)
#         print(self._job)


# obj = Pchild()
# #print("hello",obj.age) # error

