# -*- coding: utf-8 -*-
# Copyright 2019, Axel Zedigh, All rights reserved.

import csv, string, random, time, copy

class Pokemon():

	def __init__(self, name, nr=1, HP=30, Atk=20, Def=30, Type1="Normal", Mass=10):
		self.nr = float(nr)
		self.name = str(name)
		self.HP = int(HP)
		self.Atk = int(Atk)
		self.Def = int(Def)
		self.Type1 = str(Type1)
		self.Mass = float(Mass)

	def __str__(self):
		return str("HP:{}\t Atk:{}\t Def:{}\t Type1:{}\t Mass:{}\t [{}]".format(
			self.HP,self.Atk,self.Def,self.Type1,self.Mass,self.name))

	def __lt__(self,other):
		return self.Mass < other.Mass

	def fight(self,other):
		"""Två Pokemon slåss mot varandra. 
		Indata är den andra pokemonen
		Utdata är 1 vid vinst eller 1 vid förlust mot den andra pokemonen.
		Tyngre pokemons har fördel: får börja samt har fördel (rel. viktskillnad) i Atk.
		Den pokemon som når 0 HP eller mindre först förlorar.
		"""
		massDiff = self.Mass - other.Mass 	#Skillnad i vikt
		relMassAdv = (1-float((max(self.Mass, other.Mass)-abs(massDiff))/(
			max(self.Mass, other.Mass)))) #relativ massskillnad

		#Den tyngre pokemonen får börja fighten och har fördel i Atk
		if self > other:
			i = 1
			selfAtk = round(self.Atk//4 + (self.Atk//4)*relMassAdv)
			otherAtk = round(other.Atk//4)
		else:
			i = 0
			selfAtk = round(self.Atk//4)
			otherAtk = round(other.Atk//4 + (other.Atk//4)*relMassAdv)

		#Fight!
		while (self.HP > 0 and other.HP > 0):
			if i%2 ==1:
				damage = round(otherAtk*random.random())
				other.HP = other.HP - damage
				print("{} attack!\t({} damage)".format(self.name, damage))
				print(str("{}'s HP: {}".format(other.name, other.HP)))
				print("")
				time.sleep(1)
				i += 1
			else:
				damage = round(otherAtk*random.random())
				self.HP = self.HP - damage
				print("{} attack!\t({} damage)".format(other.name, damage))
				print(str("{}'s HP: {}".format(self.name, self.HP)))
				print("")
				time.sleep(1)
				i += 1

		#Skriva ut vem som vann
		time.sleep(0.4)
		if self.HP > other.HP:
			print(str("{} is the winner!".format(self.name)))
			print("")
			return(1)
		else:
			print(str("{} is the winner!".format(other.name)))
			print("")
			return(-1)

	def mate(self,other):
		"""Två Pokemon får barn"""
		pass

	def runAway(self):
		pass

class Gym():

	def __init__(self, members =[]):
		self.members = []
		self.antal = len(self.members)

	def __str__(self):
		lista = []
		for pk in self.members:
			lista.append(pk.name)
		lista.sort()
		return str(lista)

	def findMember(self):
		"""Sök efter medlemmar i gymmet 
		(läggs till efter att man skapar Teams).
		Indata är namnet på den sökta Pokemonen.
		Utdata är utskrift"""
		name = input("What pokemon do you want to lookup? ('q'to quit) ")
		while name != "q":
			i = 0
			for mbr in self.members:
				if mbr.name == name:
					print("")
					print("Yes, {} is a member.".format(name))
					i +=1
					break
			if i == 0:
				print("")
				print("No, {} is not a member.".format(name))
			name = input("What pokemon do you want to lookup? ('q'to quit) ")

	def createTeam(self, antal, pokedex):
		"""Skapar ett team av slumpade pokemons.
		Indata är antalet pokemons i teamet samt den pokedex som 
		man vill plocka pokemons från.
		Utdata är en lista med pokemon-objekt."""
		self.Team = []
		for i in range(antal):
			self.Team.append(pokedex[slumpaPkNr()])
			self.members.append(self.Team[i])
		return self.Team

	def printTeam(self, team):
		"""Skriver ut teamet snyggt.
		Indata är lista med pokemonobjekt."""
		print("Pokemon in team:")
		for pk in team:
			print(pk.name)
		print("")

	def fightTeam(self, Team1, Team2):
		"""Skapar en teamfight mellan två rivaliserande lag.
		Indata är lista med pokemonobjekt, team1, och för team2.
		Dessa listor skapas med metoden createTeam().
		OBS! Teamen måste vara lika stora.
		I slutet av fighten skrivs vinnande laget ut på skärmen."""
		if len(Team1) == len(Team2):
			i = 0
			for pokemon in Team1:
				i += pokemon.fight(Team2[i])
			if i == 0:
				print("It's a draw!")
			elif i > 0:
				print("Team1 is the winner!")
			else:
				print("Team2 is the winner!")

def lasaFil():
	Pkdx=[]
	with open("Excel Pkdx V5.14 - Pokedex.csv", newline="") as csvfile:
		filLista = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in filLista:
			if row[0] != 'Per':
				pkmn = copy.deepcopy(row[2])
				pkmn = Pokemon(row[2], row[0], row[3], row[4], row[5], row[10], row[16][:-3])
				Pkdx.append(pkmn)
				#print("{} inserted!".format(pkmn.name))
	return Pkdx

def slumpaPkNr():
	return round((662-1)*random.random())

def slumpMatch(pokedex):
	A=slumpaPkNr()
	B=slumpaPkNr()
	print(str(pokedex[A]))
	print(str(pokedex[B]))
	print("")
	time.sleep(5)
	pokedex[A].fight(pokedex[B])
	print("")

def hardKod1():
	P = Pokemon("Bengt",1,33,44,50,"Monster",20)
	B = Pokemon("Tord")
	print(str(P))
	print(str(B))
	print(B > P)

def main():
	pokedex = lasaFil()
	#slumpMatch(pokedex)
	gym = Gym()
	Team1 = gym.createTeam(3,pokedex)
	Team2 = gym.createTeam(3,pokedex)
	gym.printTeam(Team1)
	gym.printTeam(Team2)
	#gym.fightTeam(Team1, Team2)
	print(str(gym))
	gym.findMember()

if __name__ == "__main__":
	print("")
	main()
	#hardKod1()