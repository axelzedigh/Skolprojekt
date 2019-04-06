from linkedQfile6 import LinkedQ
from hashtest import *
from molgrafik import *

LETTER = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
atoms = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg','Al', 'Si', 'P', 'S', 'Cl', 'Ar']
num = ['0','1','2','3','4','5','6','7','8','9']

def readformel(molekyl):
    for i in molekyl:
        q.enqueue(i)
    mol = readmol()
    if q.isEmpty() == False:
        raise SyntaxError("Felaktig gruppstart ")
    return mol

def readmol():
    mol = readgroup()
    if q.peek() != None and q.peek() != ")":
        mol.next = readmol()
    return mol

def readgroup():
    rutan = Ruta()

    if q.peek() == "(":
        q.dequeue()
        rutan.down = readmol()
        if q.peek() != ")":
            raise SyntaxError("Saknad högerparentes ")
        else:
            q.dequeue()
            number = readnum()
            if number == "":
                raise SyntaxError("Saknad siffra ")
            else:
                rutan.num = number

    else:
        atom = readatom()
        if atom != False:
            rutan.atom = atom
            number = readnum()
            if number != "":
                rutan.num = number
        else:
            raise SyntaxError("Felaktig gruppstart ")
    return rutan

def readatom():
    if q.peek() in letter:
        raise SyntaxError("Saknad stor bokstav ")

    if q.peek() in LETTER:
        atom = q.dequeue()
        if q.peek() in letter:
            atom = atom + q.dequeue()
        if atom in atoms:
            return atom
        else:
            raise SyntaxError("Okänd atom ")
    else:
        return False

def readnum():
    number = ""
    if q.peek() == "0":
        q.dequeue()
        raise SyntaxError("För litet tal ")

    while q.peek() in num:
        number = number + q.dequeue()
    if number == "1":
        raise SyntaxError("För litet tal ")
    if number == "":
        return number
    else:
        return int(number)

def readweight(mol):
    if mol.atom == "()" :
        molweight = readweight(mol.down)
        molweight = mol.num * molweight
        if mol.next != None:
            molweight += readweight(mol.next)
        return molweight
    else:
        atom = hashtabell.search(mol.atom)
        molweight = mol.num * atom.vikt
        if mol.next != None:
            molweight += readweight(mol.next)
        return molweight

q = LinkedQ()
mg = Molgrafik()
atomlista = skapaAtomlista()
hashtabell = lagraHashtabell(atomlista)

def main():

    molekyl = input("Skriv in en molekyl, 0 om du vill avsluta")
    while molekyl != "0":
        try:
            mol = readformel(molekyl)
            #print ("Formeln är syntaktiskt korrekt")
            vikt = readweight(mol)
            print("Molekylen väger",vikt,"mol")
            mg.show(mol)
        except SyntaxError as wrong:
            fail = ""
            while not q.isEmpty():
                fail += (q.dequeue())
            if fail != "":
                fail = " " + fail
            print(wrong, "vid radslutet", fail,sep="")
        molekyl = input("Skriv in en molekyl, 0 om du vill avsluta")
    print("Tack")
main()

#Si(C3(COOH)2)4(H2O)7