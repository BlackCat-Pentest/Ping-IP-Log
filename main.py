from threading import Thread
import os

class Th(Thread):
	def __init__(self, num):
		Thread.__init__(self)
		self.num = num
		
	def run(self):
		 os.system("ping 192.168.1.%i >> %s" %(self.num, self.num))
		 

for x in range(1, 100):
	a = Th(x)
	a.start()
