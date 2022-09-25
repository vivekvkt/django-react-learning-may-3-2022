from threading import Thread
from threading import * 

# def main_thread():
#     for i in range(4): 
#         print("child thread")
    
    
# t = Thread(target=main_thread)
# t.start()
# for i in range(4):
#     print("main threading")


# class Test:
#      def child_thread(self):
#          for i in range(4):
#              print("child thread....")


# obj = Test()
# t = Thread(target=obj.child_thread)
# t.start()
# for i in range(4):
#     print("main threading ... ")

import time
class JoinThread:
    def join(self):
        print("child thread started......")
        time.sleep(4) 
obj = JoinThread()
t = Thread(target=obj.join)
t.start()
t.join()

for i in range(4):
    print("main thread started.......")


