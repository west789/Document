import threading
import time

class Num:
    def __init__(self):
        self.num = 0
        self.lock = threading.Lock()
    
    def add(self):
        self.lock.acquire()
        self.num += 1
        num = self.num
        self.lock.release()
        return num

class jdThread(threading.Thread):
    def __init__(self, item):
        threading.Thread.__init__(self)
        self.item = item
    
    def run(self):
        time.sleep(1)
        value = n.add()
        print(self.item, value)
    

n = Num()
for item in range(100):
    t = jdThread(item)
    t.start()
    t.join()