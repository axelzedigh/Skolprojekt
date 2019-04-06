__author__ = 'Marcus'

import string

class LinkedQ(object):

    def __init__(self):#Definierar first och last i "listan"
        self.first = None
        self.last = None

    def __str__(self):#Skapar en str för utskrift
        sträng = ""
        kort = self.first
        while kort != None:#Så länge listan är fyld ska programmet lägga till värden ur listan till strängen
            sträng = sträng + str(kort.value) + " "
            kort = kort.nästa
        return sträng

    def enqueue(self,x):#Läger in föremål i kön
        ny_node = Node(x)

        if self.last == None:#Om listan är tom ska det nya objektet klassas som både första och sista
            self.first = ny_node
            self.last = ny_node
        else:
            self.last.placera_nästa(ny_node)#Annars ska det läggas till en ny och de gamla förflyttas
            self.last = ny_node

    def dequeue(self):#Tar ut föremål ur kön
        if self.first == None:#Är listan tom så ska den inte röras
            pass
        elif self.first == self.last:#Finns det bara ett föremål i listan så ska "first och last" tömmas
            kö_värde = self.first
            self.first = None
            self.last = None
            return kö_värde.value
        else:#Ta ut och returna det första värdet och flytta fram de andra ett steg
            kö_värde = self.first
            self.first = self.first.nästa
            return kö_värde.value

    def isEmpty(self):#Kollar om kön är tom
        if self.first == None:
            return True
        else:
            return False

    def peek(self):
        if self.first != None:
            next_value = self.first
            return next_value.value
        else:
            return None


class Node(object):#Node klass som skapar kopplingar mellan listobjekten

    def __init__(self, value, nästa = None):
        self.value = value
        self.nästa = nästa

    def placera_nästa(self, ny_node):#Skapar kopplingen mellan objekten
        self.nästa = ny_node

class Syntaxfel(Exception):
    pass