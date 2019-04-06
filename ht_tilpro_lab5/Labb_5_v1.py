# -*- coding: iso-8859-1 -*-

#Labb 5 v.1

from Tkinter import *
import Labb_2_4

class Kryssruta(Button):
	""" Knapp som kryssas i/ur när man trycker på den """
	
	def __init__(self, master = None, nr = 0):
		Button.__init__(self, master)
		self.master = master
		self.nr = nr
		global antaltryck
		antaltryck = 1
		self["command"] = self.nedtryckt
		#self.bind("<Enter>", self.fokus)

	def nedtryckt(self):
		"""Vad som sker när knappen trycks ner"""
		global antaltryck
		antaltryck += 1
		self["text"] = antaltryck
		rest = antaltryck % 2
		if rest == 0:
		    self["text"] = "X"
		elif rest == 1:
		    self["text"] = "O"
		#else:
		    #self["text"] = "O"
		self.master.uppdateraInfo(self.nr);
		self.master.kollaMatris()
		self.master.sparaMatris()

	def fokus(self, event):
		self.master.inforad["text"] = "Knapp " + str(self.nr+1) + " övervägs   "

class KnappMatris(Frame):
	""" En lista med kryssrutor som ritas som en matris """

	def __init__(self, master = None, rader =12, kolumner = 12):
		Frame.__init__(self, master)
		self.filnamn = filnamn
		self.grid()
		self.rader = rader
		self.kolumner = kolumner
		self.antal = rader*kolumner
		self.skapaKryssrutor()
		self.inforad = Label(master, text = "Kör igång!")
		self.pynta(self.inforad, bredd = (self.kolumner+2)*4)
		self.inforad.grid(row = self.rader, column = 0)
		self.inforad.grid()
		
	def pynta(self, komponent, bakgrundsfarg = "white", bredd = 3, hojd = 1, textfarg = "black", font = ("Times", 20, "normal")):
		komponent["width"] = bredd
		komponent["height"] = hojd
		komponent["bg"] = bakgrundsfarg
		komponent["fg"] = textfarg
		komponent["font"] = font
		komponent["highlightbackground"] = "grey"
		komponent["highlightcolor"] = "green"
		komponent["highlightthickness"] = 5

	def skapaKryssrutor(self):
		self.knapplista = []
		for nr in range(self.antal):
			rad = nr//self.kolumner
			kolumn = nr%self.kolumner
			ny = Kryssruta(self, nr)  
			self.pynta(ny, bakgrundsfarg="grey")
			ny.grid(row = rad, column = kolumn)
			self.knapplista.append(ny)

	def uppdateraInfo(self, id):
		self.inforad["text"] = "Ruta " + str(id+1) + " trycktes "

	def kollaMatris(self, antal_i_rad = 5):
		matris = []
		matris2 = []
		tecken = ['X', 'O']
		leta = ['rad', 'kolumn', 'diagonal']

		for line in self.knapplista:
			matris.append(line["text"])
		for x in range(1,self.rader+1):
			matris2.append(matris[self.kolumner*(x-1):((self.kolumner * x))])

		utfall_rad_X = Labb_2_4.finn_rad(matris2, 'X', antal_i_rad)
		utfall_rad_O = Labb_2_4.finn_rad(matris2, 'O', antal_i_rad)
		utfall_kolumn_X = Labb_2_4.finn_kolumn(matris2, 'X', antal_i_rad)
		utfall_kolumn_O = Labb_2_4.finn_kolumn(matris2, 'O', antal_i_rad)
		utfall_diagonal_X = Labb_2_4.finn_diagonal(matris2, 'X', antal_i_rad)
		utfall_diagonal_O = Labb_2_4.finn_diagonal(matris2, 'O', antal_i_rad)

		for tek in tecken:
			for let in leta:
				if eval('utfall_'+let+'_'+tek) == True:
					self.inforad["text"] = str(antal_i_rad) + " "+str(tek)+" i rad!"
					for knapp in self.knapplista:
						knapp["state"] = DISABLED

	def sparaMatris(self):
		file_in = open(filnamn, 'w')
		vek_matris = []
		for line in self.knapplista:
			vek_matris.append(line["text"])
		for x in range(1,self.rader+1):
			file_in.write(str(vek_matris[self.kolumner*(x-1):((self.kolumner * x))])+'\n')
		file_in.close()

def main(fil):
	print fil
	global filnamn
	filnamn = fil
	rot = Tk()
	matris = KnappMatris(rot)
	matris.mainloop()

if __name__ == "__main__":
	main('1.txt')