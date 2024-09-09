import os
lista = [45, 55, 3]

def Mostrar(XD):
    print(XD)
    
def OL(a):
    a.sort()
    Mostrar(a)

def RL(a):
    a.sort(reverse=True)
    Mostrar(a)

def AL(a):
    a.append(99)
    Mostrar(a)

def SL(a):
    a.pop(0)
    Mostrar(a)

def Il(a):
    a.insert(3, 30)
    Mostrar(a)

def removeL(a):
    a.remove(30)
    Mostrar(a)


    
print(lista)
OL(lista)
RL(lista)
AL(lista)
SL(lista)
Il(lista)
removeL(lista)


os.system("pause")