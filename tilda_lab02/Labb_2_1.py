# -*- coding: iso-8859-1 -*-

from array import array

class ArrayQ():


	def __init__(self, __stack = None, master = None):
		global card, card_2, a
		self.__stack = array('i')

	def enqueue(self, nr):
		self.__stack.append(nr)

	def dequeue(self):
		return self.__stack.pop(0)

	def isEmpty(self):
		if self.__stack == array('i'):
			print("Kön är tom")
		else:
			print("Kön är inte tom")
	def trolleri(self):
		card = str(raw_input('Skriv kortordning med mellanslag: '))
		card = card.split()
		#Konvrtera strängar till integers:
		#card_2 = []
		#for i in range(len(card)):
		#	a = int(card[i])
		#	card_2.append(a)
		card_2 = []
		for i in range(len(card)):
			tmp = card.pop(0)		#spara tillfälligt
			#print card, tmp
			#print ' '
			card.append(tmp)		#lägg till i slutet
			card_2.append(card[0])	#lägg till andra elemtet i
			card.pop(0)
			#print i, card, card_2
		print (card_2)
		return card_2
		# 8 1 6 2 10 3 7 4 9 5 --> 1-10 i ordning

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
	s = ArrayQ()
	q.trolleri()


if __name__ == "__main__":
	
