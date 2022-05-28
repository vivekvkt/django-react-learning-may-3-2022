def generators():
    n = 10
    yield n
    n +=1
    yield n 
    
x = generators()
print(next(x))
print(next(x))