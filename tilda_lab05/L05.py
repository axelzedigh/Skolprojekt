
# -*- coding: utf-8 -*-
# Copyright 2019, Axel Zedigh, All rights reserved.

import copy, linkedQFile
from L03 import Bintree, Node
from sys import exit

class ParentNode():

	def __init__(self, word, parent = None):
		self.word = word
		self.parent = parent

class Bfs():

	def __init__(self):
		self.barnlista = []
		self.gamla = Bintree()
		self.svenskaordlista = svensk()
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
		self.queue.enqueue(ParentNode(self.startord))
		while self.queue.isEmpty != True:
			nod = self.queue.dequeue()
			self.makeChildren(nod)
		print("Det finns inte en väg!")

	def writeChain(self, nod):
		if nod != None:
			self.writeChain(nod.parent)
			print(nod.word, sep=" ", end=" ")

	def makeChildren(self, nod):
		if nod.word == self.slutord:
			self.writeChain(nod)
			print("")
			exit()
		if nod.word in self.svenskaordlista:
			if nod.word not in self.gamla:
				self.gamla.put(nod.word)
				for i in range(3):
					for j in range(len(self.alfabet)):
						nyord = list(copy.deepcopy(nod.word))
						nyord[i] = self.alfabet[j]
						nyord = "".join(nyord)
						if nyord in self.svenskaordlista:
							if nyord not in self.gamla:
								nynod = ParentNode(nyord, nod)
								self.queue.enqueue(nynod)

def svensk():
	svenska = Bintree()
	with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
		for rad in svenskfil:
			ordet = rad.strip() # Ett trebokstavsord per rad
			if ordet not in svenska:
				svenska.put(ordet) # in i sökträdet
	return svenska

def main2():
	b = Bfs()
	b.breddFirstSearch()

def utskrift1(lista):
	if len(lista) > 0:
		print(lista[0])
		utskrift1(lista[1:])

def utskrift2(lista):
	if len(lista) > 0:
		utskrift2(lista[1:])
		print(lista[0])

def main1():
	lista = [1,2,3,4,5]
	utskrift1(lista)
	utskrift2(lista)

if __name__ == "__main__":
	#main1()
	main2()