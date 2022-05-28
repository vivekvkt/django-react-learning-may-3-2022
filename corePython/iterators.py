class ListIterator:
    
    def __init__(self, a):
        self.__list = a
        self.__index = -1
        
    
    def __iter__(self):
        return self
    
    
    def __next__(self):
        self.__index +=1
        if self.__index >= len(self.__list):
            raise StopIteration 
        return self.__list[self.__index]
    

a = [1,2,3,4,5]
myList = ListIterator(a)
it = iter(myList)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

    