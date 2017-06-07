import math
class Vector(object):
	def __init__(self,v1):
		self.v1 = v1
	def add(self,v2):
		self.arr = [1,2,3]
		for i in range(0,len(self.v1)):
			self.arr[i] = self.v1[i] + v2.v1[i]
		print self.arr
	def subtract(self,v2):
		self.arr = []
		for i in range(0,len(self.v1)):
			self.arr.append(self.v1[i] - v2.v1[i])
		print self.arr
	def dot(self,v2):
		self.store = 0
		for i in range(0,len(self.v1)):
			self.store+=self.v1[i] * v2.v1[i]
		print self.store
	def norm(self):
		self.collect = 0
		for i in range(0,len(self.v1)):
			self.collect+=(self.v1[i])**2
		print math.sqrt(self.collect)

a = Vector([1,2,3])
b= Vector([3,4,5])
a.add(b)
a.subtract(b)
a.dot(b)
a.norm()