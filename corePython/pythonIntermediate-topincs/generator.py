# def generators():
#     n = 10
#     yield n
#     n +=1
#     yield n 
    
# x = generators()
# print(next(x))
# print(next(x))

# def firstnumber(num):
#     n = 1
#     while n <= num:
#       yield n 
#       n = n+1
      
      
# values = firstnumber(4)
# for  i in values:
#     print(i) 


# def fib():
#     a,b = 0,1
#     while True:
#         yield a 
#         a,b = b , a+b
# for f in fib():
#     if f > 80:
#         break
#     print(f) 


# l = (x*x for x in range(10000000000000000))
# print(next(l))


# class Square:
#     def __init__(self, length) -> None:
#        self.length = length
#        self.current = 0 
       
       
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         result = self.current ** 2
#         self.current += 1
        
#         if self.current > self.length:
#             raise StopIteration
#         return result
    
    
# length = 5
# square = Square(length)
# for s in square:
#     print(s)



