# -*- coding: utf-8 -*-
# Copyright 2019, Axel Zedigh, All rights reserved.

import copy, linkedQFile
from L03 import Bintree, Node
from sys import exit

class Bfs():

	def __init__(self):
		self.barnlista = []
		self.gamla = Bintree()
		self.svenskaordlista = svensk()
		self.dict = {}
		self.queue = linkedQFile.LinkedQ()
		self.ordgang = []
		self.alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

	def breddFirstSearch(self):
		self.startord = input("Startord: ")
		while self.startord not in self.svenskaordlista:
			self.startord = input("Startordet finns ej i ordbok, försök igen: ")
		self.slutord = input("Slutord: ")
		while self.slutord not in self.svenskaordlista:
			self.slutord = input("Slutordet finns ej i ordbok, försök igen: ")
		self.queue.enqueue(self.startord)
		while self.queue.isEmpty != True:
			nod = self.queue.dequeue()
			self.makeChildren(nod)
		print("det finns inte en väg!")

	def makeChildren(self, ordet):
		if ordet == self.slutord:
			print("Det finns en väg till " +str(self.slutord))
			exit()
		if ordet in self.svenskaordlista:
			if ordet not in self.gamla:
				self.gamla.put(ordet)
				for i in range(3):
					for j in range(len(self.alfabet)):
						nyord = list(copy.deepcopy(ordet))
						nyord[i] = self.alfabet[j]
						nyord = "".join(nyord)
						if nyord in self.svenskaordlista:
							if nyord not in self.gamla:
								self.queue.enqueue(nyord)

def svensk():
	svenska = Bintree()
	with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
		for rad in svenskfil:
			ordet = rad.strip() # Ett trebokstavsord per rad
			if ordet not in svenska:
				svenska.put(ordet) # in i sökträdet
	return svenska

def main():
	b = Bfs()
	b.breddFirstSearch()

if __name__ == "__main__":
	main()