import time

def fib(n):
    a , b = 0,1
    while n >0:
        yield b
        a,b = b, a+b
        n -=1
n= 9
g = fib(n)

try:
    for e in g:
        print(e)
        time.sleep(1)
except KeyboardInterrupt:
    print("Calculation Stoped !")