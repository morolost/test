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

mostrar_1_al_10()

os.system("pause")

def mostrar_numeros_ascendente():
    inicio = int(input("Introduce el número de inicio(menor): "))
    fin = int(input("Introduce el número de fin(mayor): "))
    for i in range(inicio, fin + 1):
        print(i)

def mostrar_numeros_descendente():
    inicio = int(input("Introduce el número de inicio(mayor): "))
    fin = int(input("Introduce el número de fin(menor): "))
    for i in range(inicio, fin - 1, -1):
        print(i)
        
mostrar_numeros_ascendente()

os.system("pause")

mostrar_numeros_descendente()