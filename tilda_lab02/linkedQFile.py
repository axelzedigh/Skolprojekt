# -*- coding: iso-8859-1 -*-

class Node():
	"""Skapar nodobjekt med ett data-attribut och next-pekare"""
	def __init__(self, data, next = None):
		self.data = data
		self.next = next
class LinkedQ():
	"""
	En länkad kö som lägger in noder med metoden .enqueue, 
	tar ut med .dequeue, kollar om tom med .isEmpty, tittar på
	första och sista elementet med .peek_first, .peek_last samt
	skriver ut kö med .printQ
	"""
	def __init__(self):
		self.first = None
		self.last = None
		self.count = 0

	def __str__(self):
		xoxo = []
		k = self.first
		while k is not None:
			xoxo.append(k.data)
			k = k.next
		return str(xoxo)

	def __len__(self):
		return self.count

	def enqueue(self, value):
		new_node = Node(value)
		if self.last is None:
			self.first = self.last = new_node
			self.count += 1
			return
		self.last.next = new_node
		self.last = new_node
		self.count += 1

	def dequeue(self):
		if self.isEmpty():
			return
		huvud = self.first
		self.first = self.first.next
		self.count -= 1
		if self.first == None:
			self.last = None
		return huvud.data

	def isEmpty(self):
		if self.first is None and self.last is None:
			return True
		else:
			return False

	def peek_first(self):
		return self.first.data

	def peek_last(self):
		return self.last.data

	def printQ(Queue):
		print(str(Queue) + " är för tillfället inlagt!")

def main1():
	q = LinkedQ()
	q.enqueue(1)
	q.enqueue(2)
	x = q.dequeue()
	y = q.dequeue()
	if (x == 1 and y == 2):
		print("Fungerar")
	else:
		print("Något är fel. 1 och 2 förväntades men vi fick", x, y)

def main2():
	Q = LinkedQ()
	print (Q.__doc__)
	print ("Är tom?: " + str(Q.isEmpty()))
	Q.enqueue("Vill")
	Q.enqueue("du")
	Q.enqueue("ha")
	Q.enqueue("en")
	Q.enqueue("tomat")
	Q.printQ()
	Q.enqueue("ikvall")
	Q.enqueue("som")
	Q.enqueue("beloning")
	print ("Är tom?: " + str(Q.isEmpty()))
	Q.dequeue()
	Q.dequeue()
	Q.dequeue()
	Q.dequeue()
	Q.printQ()
	print (len(Q))

if __name__ == "__main__":
	main1()