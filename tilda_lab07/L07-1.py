# -*- coding: utf-8 -*-
# Copyright 2019, Axel Zedigh, All rights reserved.

import timeit, copy

class DictHash(object):
	
	def __init__(self):
		self.dict = {}

	def __contains__(self,key):
		if key in self.dict.keys():
			return True
		elif key in self.dict.values():
			return True
		else:
			return False

	def __setitem__(self,key,value):
		self.dict[key] = value

	def __getitem__(self,key):
		return self.search(key)

	def store(self, key, value):
		self.dict[key] = value

	def search(self, key):
		if key in self.dict.keys():
			return self.dict[key]
		else:
			raise KeyError("Nyckel verkar inte finnas i dictionary")

def filinlasning(filename, dictionary):
	with open(filename, "r", encoding = "utf-8") as fil:
		for line in fil:
			info = line.split("\t")
			artistnamn = info[1]
			lattitel = info[2]
			dictionary[artistnamn] = lattitel
	return

def _tidtagning():
	h = DictHash()
	filinlasning("sang10000rader.txt",h)

def tidtagning(varv):
	tid = timeit.timeit(stmt = lambda: _tidtagning(), number = varv)
	print("Det tog",tid,"sekunder att lägga in 10000rader i dict",varv,"gånger.")

if __name__ == "__main__":
	y = DictHash()
	y["Axel"] = 739849816
	y.store("Henrik", 736452877)
	if "Henrik" in y: print(True)
	if 739849816 in y: print(True)
	x = y.search("Axel")
	print("x =",x)
	tidtagning(100)

