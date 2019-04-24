
import threading
from threading import Thread
import time
 
thnum=0
 
class MyThread(threading.Thread):
	def run(self):
		for i in range(10000):
			global thnum
			thnum+=1	
		print(thnum)
 
def test():
	global thnum
	for i in range(10000):
		thnum+=1
	print(thnum)
if __name__=='__main__':
    
    
    t=MyThread()
    t.start()
    # time.sleep(4)
    test()
    t.join()
