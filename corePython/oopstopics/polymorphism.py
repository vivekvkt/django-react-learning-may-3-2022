class Beans:
    def type(self):
        print("hello beans")
    def color(self):
        print("green hello")
        
class Deans:
    def type(self):
        print("hello dands")
    def color(self):
        print("hello colore deans")
        
        
def fun(obj):
    obj.type()
    obj.color()
    
obj1 = Beans()
obj2 = Deans()
fun(obj1)
fun(obj2)