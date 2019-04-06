# -*- coding: utf-8 -*-
# Copyright 2019, Axel Zedigh, All rights reserved.

from L03 import Bintree, Node

def svensk():
	svenska = Bintree()
	with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
		for rad in svenskfil:
			ordet = rad.strip() # Ett trebokstavsord per rad
			if ordet in svenska:
				pass
			else:
				svenska.put(ordet) # in i sökträdet
	return svenska

def engelsk(svenska):
	engelska = Bintree()
	with open("engelska.txt", "r", encoding = "utf-8") as engelskfil:
		for rad in engelskfil:
			ordet = rad.split() # Ett trebokstavsord per rad
			for word in ordet:
				if word in engelska:
					pass
				else:
					if word in svenska:
						print(word, end = " ")
					engelska.put(word) # in i sökträdet
		print("\n")

if __name__ == "__main__":
	s = svensk()
	engelsk(s)