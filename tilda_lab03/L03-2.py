# -*- coding: iso-8859-1 -*-
# Copyright 2019, Axel Zedigh, All rights reserved.

from L03 import Bintree, Node

def main():
	svenska = Bintree()
	with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
		for rad in svenskfil:
			ordet = rad.strip() # Ett trebokstavsord per rad
			if ordet in svenska:
				print(ordet, end = " ")
			else:
				svenska.put(ordet) # in i sökträdet
		print("\n")

if __name__ == "__main__":
	main()