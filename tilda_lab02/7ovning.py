from queue import Queue
from sys import exit

class Node:
    def __init__(self, tal = 0, op = "", far = None):
        self.tal = tal
        self.op = op
        self.far = far


def insert(tal, op, far):
    nod=Node(tal, op, far)
    q.put(nod)

def makesons(far):
    tal = far.tal
    if tal == 108:
        writechain(far)
        exit()
    insert(tal+7, "+", far)
    insert(tal-7, "-", far)
    insert(tal*7, "*", far)
    if(tal%7==0): 
        insert(tal/7, "/", far)

def writechain(p):
    if p != None: 
        writechain(p.far)
        if p.far != None:
            print(p.op, "7 =",  p.tal)
        else:
            print(p.tal)

if __name__ == "__main__":
    q=Queue()
    q.put(Node())             
    while not q.empty():
        makesons(q.get()) 