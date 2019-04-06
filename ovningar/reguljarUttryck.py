# -*- coding: iso-8859-1 -*-

import re

class sokText():

	def __init__(self):
		self.inlastText = ""

	def fillasning(self):
		with open("textMedNamn.txt", "r", encoding = "utf-8") as historia:
			self.text = historia.readlines()
			return str(self.text)

	def regEg(self):
		self.expr = "[A-Z]*[a-z]+[Gg]+[a-z]+"
		self.text = self.fillasning()
		print (self.text + "\n")	
		print (re.findall(self.expr, self.text))

if __name__ == "__main__":
	r = sokText()
	r.regEg()