# -*- coding: iso-8859-1 -*-

from arrayQFile import ArrayQ
from linkedQFile import LinkedQ, Node

class TrolleriTrick():

	def __init__(self):
		#self.card = LinkedQ()
		self.card = ArrayQ()
		self.trolleri()

	def trolleri(self):
		self.input = input('Skriv kortordning med mellanslag: ')
		self.input = self.input.split(' ')
		for i in self.input:
			i = int(i)
			self.card.enqueue(i)
		while self.card.isEmpty() != True:
			self.card.enqueue(self.card.dequeue())
			print(self.card.dequeue(),sep=" ", end=" ")
		print("")

def main():
	TrolleriTrick()

if __name__ == "__main__":
	main()