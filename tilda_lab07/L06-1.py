# -*- coding: utf-8 -*-
# Copyright 2019, Axel Zedigh, All rights reserved.

import timeit, copy

class Song():

	def __init__(self, trackid = None, lattid = None, artistnamn = None, lattitel = None, artistid = None, latlangd = None, ar = None):
		self.trackid = trackid
		self.lattid = lattid
		self.artistnamn = artistnamn
		self.lattitel = lattitel
		self.artistid = artistid
		self.latlangd = latlangd
		self.ar = ar

	def __lt__(self, other):
		return self.artistnamn < other.artistnamn

	def __str__(self):
		return "{}\t{}\t{}\t{}\t{}\t{}\t{}".format(self.trackid,
			self.lattid,self.artistnamn,self.lattitel,self.artistid,
			self.latlangd,self.ar)

class Songlists():

	def __init__(self):
		#self.ulist500L, self.ulist500D = self.fillasningUniq("unique500rader.txt")
		#self.ulist1000L, self.ulist1000D = self.fillasningUniq("unique1000rader.txt")
		#self.ulist10000L, self.ulist10000D = self.fillasningUniq("unique10000rader.txt")
		#self.ulist100000L, self.ulist100000D = self.fillasningUniq("unique100000rader.txt")
		#self.ulistAllL, self.ulistAllD = self.fillasningUniq("unique_tracks.txt")

		self.slist50L, self.slist50D = self.fillasningSong("sang50rader.txt")
		self.slist500L, self.slist500D = self.fillasningSong("sang500rader.txt")
		self.slist1000L, self.slist1000D = self.fillasningSong("sang1000rader.txt")
		self.slist10000L, self.slist10000D = self.fillasningSong("sang10000rader.txt")
		self.slist100000L, self.slist100000D = self.fillasningSong("sang100000rader.txt")
		#self.slistAllL, self.slistAllD = self.fillasningSong("sang-artist-data.txt")

	def fillasningUniq(self, filename):
		inlastfilLista = []
		inlastfilDict = {}
		with open(filename, "r", encoding = "utf-8") as fil:
			for line in fil:
				info = line.split("<SEP>")
				song = Song(trackid = info[0], lattid = info[1], artistnamn = info[2], lattitel = info[3])
				inlastfilLista.append(song)
				inlastfilDict[info[2]] = song
		return inlastfilLista, inlastfilDict

	def fillasningSong(self, filename):
		inlastfilLista = []
		inlastfilDict = {}
		with open(filename, "r", encoding = "utf-8") as fil:
			for line in fil:
				info = line.split("\t")
				song = Song(artistid = info[0],artistnamn = info[1],lattitel = info[2], latlangd = info[3], ar = info[4])
				inlastfilLista.append(song)
				inlastfilDict[info[1]] = song
		return inlastfilLista, inlastfilDict

def printList(lista):
	for obj in lista:
		print(obj)

def SortLista(lista,metod,attr):
	sortedLista = copy.deepcopy(lista)
	if str(metod) is "m":
		mergeSort(sortedLista,attr)
	elif str(metod) is "q":
		quickSort(sortedLista,attr)
	else:
		raise KeyError("-m for mergesort, -q for quicksort")
	sistSortedLista = getattr(sortedLista[(len(sortedLista)-1)],attr)
	return sortedLista, sistSortedLista

def linjSok(lista):
	sistLista = lista[(len(lista)-1)]
	key = sistLista.artistnamn
	for song in lista:
		if song.artistnamn == key:
			#print(True)
			return True
	#print(False)
	return False

def binSearch(lista, key,attr):
	low = 0
	high = len(lista)-1
	found = False

	while low <= high and not found:
		middle = (low + high)//2
		if getattr(lista[middle],attr) == key:
			found = True
		else:
			if key < getattr(lista[middle],attr):
				high = middle -1
			else:
				low = middle + 1
	#print(key)
	#print(found)
	return found

def dictSearch(dictionary,key):
	if key == dictionary[key].artistnamn:
		#print(True)
		return True
	else:
		#print(False)
		return False
		
def quickSort(arr,attr):
	#https://www.geeksforgeeks.org/python-program-for-quicksort/
	_quickSort(arr,0,len(arr)-1,attr)

def _quickSort(arr,low,high,attr):
	if low < high:
		pi = partiotion(arr,low,high,attr)
		_quickSort(arr,low,pi-1,attr)
		_quickSort(arr,pi+1,high,attr)

def partiotion(arr,low,high,attr):
	i = (low-1) 				#index of smaller element
	pivot = arr[high]

	for j in range(low, high):
		# If current element is smaller than or equal to pivot

		if getattr(arr[j],attr) <= getattr(pivot,attr):
			# increment index of smaller element
			i = i+1
			arr[i],arr[j] = arr[j],arr[i]

	arr[i+1],arr[high] = arr[high],arr[i+1]
	return (i+1)

def mergeSort(arr,attr):
	if len(arr) >1: 
		mid = len(arr)//2 #Finding the mid of the array 
		L = arr[:mid] # Dividing the array elements  
		R = arr[mid:] # into 2 halves 
  
		mergeSort(L,attr) # Sorting the first half 
		mergeSort(R,attr) # Sorting the second half 
  
		i = j = k = 0
		  
		# Copy data to temp arrays L[] and R[] 
		while i < len(L) and j < len(R): 
			if getattr(L[i],attr) < getattr(R[j],attr): 
				arr[k] = L[i] 
				i+=1
			else: 
				arr[k] = R[j] 
				j+=1
			k+=1
		  
		# Checking if any element was left 
		while i < len(L): 
			arr[k] = L[i] 
			i+=1
			k+=1
		  
		while j < len(R): 
			arr[k] = R[j] 
			j+=1
			k+=1

def songLength(lista,last=1):
	visitSongs = {}
	for i in range(last):
		longest = lista[1]
		for song in lista:
			if float(song.latlangd) > float(longest.latlangd) and (song.artistnamn,song.lattitel,song.latlangd) not in visitSongs.values():
				longest = song
				visitSongs[i] = longest.artistnamn,longest.lattitel,longest.latlangd
	#for i in range(last):
	#	print(visitSongs[i][0],":",visitSongs[i][1],":",visitSongs[i][2])
	return visitSongs[last-1]

def tidSort(lista,metod,varv):
	sorttid = timeit.timeit(stmt = lambda: SortLista(lista,metod,artistnamn), number = varv)
	print(metod,"sortering för",len(lista), "stor lista tog", round(sorttid, 4) , "sekunder för",varv,"varv.")
	print((round(sorttid/varv*1000, 4)),"sekunder för 1000 varv")

def tidLinjSearch(lista,varv):
	linjtid = timeit.timeit(stmt = lambda: linjSok(lista), number = varv)
	print("Linjsök för",len(lista), "stor lista tog", round(linjtid, 4) , "sekunder för",varv,"varv.")
	print((round(linjtid/varv*1000, 4)),"sekunder för 1000 varv")

def tidBinSearch(lista,varv):
	sorteradLista, sistLista = SortLista(lista,"m",artistnamn)
	bintid = timeit.timeit(stmt = lambda: binSearch(sorteradLista,sistLista), number = varv)
	print("Binsök för",len(lista), "stor lista tog", round(bintid, 4) , "sekunder för",varv,"varv.")
	print((round(bintid/varv*1000, 4)),"sekunder för 1000 varv")

def tidDictSearch(dictionary,varv):
	dicttid = timeit.timeit(stmt = lambda: dictSearch(dictionary,"Årabrot"), number = varv)
	print("Dictsök för",len(dictionary), "stor lista tog", round(dicttid, 4) , "sekunder för",varv,"varv.")
	print((round(dicttid/varv*1000, 4)),"sekunder för 1000 varv")

def tidLenSearch(lista,length,varv):
	lentid = timeit.timeit(stmt = lambda: songLength(lista,length), number = varv)
	print()
	print("Längdsök för",length,"längsta låten i",len(lista), "stor osorterad lista tog", round(lentid, 4) , "sekunder för",varv,"varv.")
	print((round(lentid/varv*1000, 4)),"sekunder för 1000 varv")

def tidLenSortSearch(lista,length,varv):
	lentid = timeit.timeit(stmt = lambda: _tidLenSortSearch(lista,length), number = varv)
	print("Längdsök för",length,"längsta låten i",len(lista), "stor sorterad lista tog", round(lentid, 4) , "sekunder för",varv,"varv.")
	print((round(lentid/varv*1000, 4)),"sekunder för 1000 varv")

def _tidLenSortSearch(lista,length):
	sLi, sLiSist = SortLista(lista,"m","latlangd")
	#for i in range(length):
	#	print(sLi[len(sLi)-i-1].artistnamn,":",sLi[len(sLi)-i-1].lattitel,":",sLi[len(sLi)-i-1].latlangd)
	return sLi[len(sLi)-length-1]

def testAvBinsearch(SL,attr):
	sLi, sLiSist = SortLista(SL.ulist10000L,"m",attr)
	printList(sLi)
	r = binSearch(sLi,sLiSist,attr)
	print(sLiSist,r)

def tidDel1(SL):
	#tidLinjSearch(SL.ulist500L,100000)
	#tidLinjSearch(SL.ulist1000L,100000)
	#tidLinjSearch(SL.ulist10000L,100000)
	#tidLinjSearch(SL.ulistAllL,100)
	#print("")
	#tidBinSearch(SL.ulist500L,100000)
	#tidBinSearch(SL.ulist1000L,100000)
	#tidBinSearch(SL.ulist10000L,100000)
	#tidBinSearch(SL.ulistAllL,1)
	#print("")
	#tidSort(SL.ulist500L,"m",100)
	#tidSort(SL.ulist1000L,"m",100)
	#tidSort(SL.ulist10000L,"m",100)
	#tidSort(SL.ulistAllL,"m",1)
	#print("")
	#tidSort(SL.ulist500L,"q",100)
	#tidSort(SL.ulist1000L,"q",100)
	#tidSort(SL.ulist10000L,"q",100)
	#tidSort(SL.ulistAllL,"q",1)
	#print("")
	#tidDictSearch(SL.ulist500D ,100000)
	#tidDictSearch(SL.ulist1000D,100000)
	#tidDictSearch(SL.ulist10000D,100000)
	#tidDictSearch(SL.ulist10000D,100000)
	#tidDictSearch(SL.ulistAllD,100000)
	pass

def tidDel2(SL):

	#tidLenSearch(SL.slist50L,1,1000)
	#tidLenSearch(SL.slist50L,2,1000)
	#tidLenSearch(SL.slist50L,3,1000)
	#tidLenSearch(SL.slist50L,5,1000)
	#tidLenSearch(SL.slist50L,10,1000)

	#tidLenSearch(SL.slist500L,1,10)
	#tidLenSearch(SL.slist500L,5,10)
	#tidLenSearch(SL.slist500L,10,10)
	#tidLenSearch(SL.slist500L,100,10)

	#tidLenSearch(SL.slist1000L,1,10)
	#tidLenSearch(SL.slist1000L,5,10)
	#tidLenSearch(SL.slist1000L,10,10)
	#tidLenSearch(SL.slist1000L,100,10)

	#tidLenSearch(SL.slist10000L,1,10)
	#tidLenSearch(SL.slist10000L,5,10)
	#tidLenSearch(SL.slist10000L,10,10)
	#tidLenSearch(SL.slist10000L,100,10)
	
	#tidLenSortSearch(SL.slist50L,1,1000)
	#tidLenSortSearch(SL.slist50L,2,1000)
	#tidLenSortSearch(SL.slist50L,3,1000)
	#tidLenSortSearch(SL.slist50L,5,1000)
	#tidLenSortSearch(SL.slist50L,10,1000)

	#tidLenSortSearch(SL.slist500L,1,10)
	#tidLenSortSearch(SL.slist500L,5,10)
	#tidLenSortSearch(SL.slist500L,10,10)
	#tidLenSortSearch(SL.slist500L,100,10)

	#tidLenSortSearch(SL.slist1000L,1,10)
	#tidLenSortSearch(SL.slist1000L,5,10)
	#tidLenSortSearch(SL.slist1000L,10,10)
	#tidLenSortSearch(SL.slist1000L,100,10)

	#tidLenSortSearch(SL.slist10000L,1,10)
	#tidLenSortSearch(SL.slist10000L,5,10)
	#tidLenSortSearch(SL.slist10000L,10,10)
	#tidLenSortSearch(SL.slist10000L,100,10)

	#tidLenSearch(SL.slist50L,10,1000)
	#tidLenSortSearch(SL.slist50L,10,1000)
	pass
	
def main():
	SL = Songlists()
	tidDel2(SL)
	#testAvBinsearch(SL,"artistnamn")
	#tidDel1(SL)

if __name__ == "__main__":
	main()