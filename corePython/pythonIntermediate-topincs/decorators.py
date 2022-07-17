# def function_x(fun):
#     def wraper_fun():
#         print("x"*20)
#         fun()
#         print("x"*20)
#     return wraper_fun


# def function_y(fun):
#     def wraper_fun():
#         print("y"*20)
#         fun()
#         print("y"*20)
#     return wraper_fun

# # @function_x
# # @function_y
# def say_hello():
#     print("hello world")
    
# # yes = function_decorator(say_hello)
# # yes()
# # cd
# # say_hello()

from time import time
from unittest import result
def timing(fun):
    def time_wraper(*args, **kwargs):
    
        start = time()
        result = fun(*args, **kwargs)
        end = time()
        print("total timing start and end: {}".format(end - start))
        return result
    return time_wraper

@timing
def say_timing(num):
    
    sum = 0
    for i in range(num+1):
        sum +=1
    return f"sum values is:  {sum}"

#say_yes = timing(say_timing)
print(say_timing(200000000))
    
    