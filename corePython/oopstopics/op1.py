class Test:
    a = 10
    def __init__(self):
        Test.b = 200
    def m1(self):
        Test.c = 400
    @classmethod
    def m2(cls):
        cls.d = 300
        Test.d2 = 150
        
    @staticmethod
    def m3():
        Test.e =  50
print(Test.__dict__)
        
