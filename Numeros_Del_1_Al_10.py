import os
os.system("cls")

def mostrar_1_al_10():
    for i in range(1, 11):
        print(i)

def mostrar_10_al_1():
    for i in range(10, 0, -1):
        print(i)
        
mostrar_10_al_1()

os.system("pause")
os.system("cls")

mostrar_1_al_10()

os.system("pause")
os.system("cls")

def mostrar_numeros_ascendente(): 
    for i in range(inicio, fin + 1):
        print(i)

def mostrar_numeros_descendente():
    for i in range(inicio, fin - 1, -1):
        print(i)
        


inicio = int(input("Introduce el número de inicio: "))
fin = int(input("Introduce el número de fin: "))
if inicio >= fin:
    mostrar_numeros_descendente()
else:
    mostrar_numeros_ascendente()