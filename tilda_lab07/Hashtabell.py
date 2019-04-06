# -*- coding: utf-8 -*-
# Copyright 2019, Axel Zedigh, All rights reserved.
import timeit, copy

class Hashtabell(object):
    """Tabell med krocklista"""

    def __init__(self, size):
        self.size = size
        self.tabell = (2*size)*[None]

    def __str__(self):
        j = 0
        k = []
        for i in self.tabell:
            if i != None:
                j += 1
                #print("i =",j,i.nodkey, i.nodvalue)
                k.append([j,i.nodkey,i.nodvalue])
            else:
                j +=1
                #print("i =",j,None)
                k.append([j,None,None])
        return str(k)

    def store(self,key,value):
        nameindex = self.hashfunktion(key)
        #print(nameindex)
        while self.tabell[nameindex] != None:
            nameindex += 1
        self.tabell[nameindex] = HashNod(key,value)

    def hashfunktion(self, key):
        count = 1
        keyhash = 0

        for i in key:
            charactervalue = ord(i)
            keyhash += charactervalue * count
            count = count * 32
        keyindex = int(keyhash % len(self.tabell))
        return keyindex

    def search(self, key):
        nameindex = self.hashfunktion(key)

        while self.tabell[nameindex] != None:
            if self.tabell[nameindex].nodkey == key:
                return self.tabell[nameindex]
            #elif self.tabell[nameindex].nodvalue == key:
            #   return self.tabell[nameindex], True
            else: nameindex += 1
        raise KeyError("Nyckel verkar inte finnas i dictionary")

    def __setitem__(self,key,value):
        self.store(key,value)

    def __getitem__(self, key):
        #nameindex = self.hashfunktion(key)
        return self.search(key)[0].nodvalue

    def __contains__(self, key):
        i = self.search(key)
        if i.nodkey==key:
            return True
        #elif i.nodvalue ==key:
        #   return True
        else:
            return False        

class HashNod(object):

     def __init__(self, nodkey, nodvalue):
        self.nodkey = nodkey
        self.nodvalue = nodvalue

def filinlasning(filename, dictionary):
    with open(filename, "r", encoding = "utf-8") as fil:
        for line in fil:
            info = line.split("\t")
            artistnamn = info[1]
            lattitel = info[2]
            #print(artistnamn)
            dictionary[artistnamn] = lattitel
    return

def _tidtagning():
    h = Hashtabell(10000)
    filinlasning("sang10000rader.txt",h)

def tidtagning(varv):
    tid = timeit.timeit(stmt = lambda: _tidtagning(), number = varv)
    print("Det tog",tid,"sekunder att lägga in 10000rader i Hashtabell",varv,"gånger.")

def main1():
    h.store("Henrik", "07072746")
    h.store("Axel", '073984981')
    h["Conny"] = '07432746'
    h.store("Lennart", '073983981')
    h.store("Hemler", '073224981')
    h.store("Sten", '073231981')
    print(h.search("Axel"))
    print(str(h))
    #print(getattr(h["Axel"],"nodvalue"))
    #print(getattr(h["Axel"],"nodkey"))
    #for i in h:
    #   print(getattr(i,"nodnamn"),getattr(i,"nodobjekt"))
    #'07432746' in h

def main2():
    #h = Hashtabell(10000)
    #filinlasning("sang10000rader.txt",h)
    #print(h.search("Kanye West").nodvalue)
    #if "Kanye West" in h:
    #   print("Eff ja")
    #str(h)
    tidtagning(100)
    pass


if __name__ == "__main__":
    #main2()
    pass