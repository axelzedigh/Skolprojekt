# -*- coding: iso-8859-1 -*-

from array import array

class ArrayQ():

	def __init__(self):
		self._stack = array("H")

	def __repr__(self):
		return "ArrayQ()"

	def __str__(self):
		return self._stack.tostring()

	def __len__(self):
		return len(self._stack)

	def enqueue(self, nr):
		self._stack.append(nr)

	def dequeue(self):
		return self._stack.pop(0)

	def isEmpty(self):
		if self._stack.buffer_info()[1] == 0:
			return True
		else:
			return False

def main():
	q = ArrayQ()
	q.enqueue(1)
	q.enqueue(2)
	x = q.dequeue()
	y = q.dequeue()
	if (x == 1 and y == 2):
		print("Fungerar")
	else:
		print("Något är fel. 1 och 2 förväntades men vi fick", x, y)

if __name__ == "__main__":
	main()