""" Singleton Design Pattern"""

# class Singleton:
#     __instance = None
    
#     @staticmethod
#     def getInstance():
#         """ static method """
#         if Singleton.__instance == None:
#             Singleton()
           
#         return f" 'fisrt ' {Singleton.__instance}"
    
#     def __init__(self):
#         """ virtual private constructor"""
#         if Singleton.__instance!=None:
#             raise Exception("This  class  is a singleton")
#         else:
#             Singleton.__instance = self
            
# s = Singleton()
# print("s1",s)

# s = Singleton.getInstance()
# print("s2",s)
# s = Singleton.getInstance()
# print("s3",s)

""" Factory Design Pattern"""


# class Button(object):
#     html = ""
#     def get_html(self):
#        return self.html

# class Image(Button):
#    html = "<img></img>"

# class Input(Button):
#    html = "<input></input>"

# class Flash(Button):
#    html = "<obj></obj>"

# class ButtonFactory():
#    def create_button(self, typ):
#       targetclass = typ.capitalize()
#       return globals()[targetclass]()

# button_obj = ButtonFactory()
# button = ['image', 'input', 'flash']
# for b in button:
#    print (button_obj.create_button(b).get_html())