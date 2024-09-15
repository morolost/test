"""
diccionario digital:
4)cargar archivo json 
3)actualizar
2)buscar/leer palabra y definicion 
1)agregar nuevas palabras

json.load
json.dump

5)que pasa si se pone una misma palabra con misma o distinta definicion?

"""
"""
import json

def misma_palabra():
    if palabra in diccionario:
        diccionario.remove(palabra)
        print("esta palabra ya esta")
    
def agregar_palabra(diccionario):
    palabra = input("agregar palabra: ")
    definicion = input("ingrese su definicion: ")
    registro = {palabra:definicion}
    diccionario.append(registro)
    return diccionario

def buscar_definicion_de_palabra():
    palabra=input("que palabra quiere buscar: ")
    if palabra in diccionario:
        print("esta es la definicion: ",definicion)
    else:
        agregar=int(input("desea agregar otra palabra?(si=1)"))
        if agregar == 1:
            agregar_palabra()
        else:
            print("OK")


def cargar_palabra():
    if palabra not in diccionario:
        agregar_palabra()

registro = []
palabra = ""
definicion = ""

diccionario=[palabra, definicion]
agregar_palabra(diccionario)
"""
import os
import json

os.system("cls")

"""
cargar diccionario: permite que la palabra con su definicion sea agregada a la libreria de json
guardar diccionario: 

"""
def cargar_diccionario(archivo):
    try:
        with open(archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_diccionario(diccionario, archivo):
    with open(archivo, 'w') as file:
        json.dump(diccionario, file, indent=4)

def agregar_palabra(diccionario):
    palabra = input("Introduce la palabra: ")
    definicion = input(f"Introduce la definición de '{palabra}': ")
    
    diccionario[palabra] = definicion
    print(f'Palabra "{palabra}" agregada/actualizada con definición: "{definicion}"')


def buscar_palabra(diccionario):
    palabra = input("Introduce la palabra que deseas buscar: ")
    if palabra in diccionario:
        print(f'{palabra}: {diccionario[palabra]}')
    else:
        print(f'La palabra "{palabra}" no se encuentra en el diccionario.')
        i = input("Desea agregar esa nueva palabra? si/no  ")
        if i == "si":
            agregar_palabra(diccionario)
        else:
            print("el diccionario no se ha modificado...")

def actualizar_palabra(diccionario):
    palabra = input("Introduce la palabra que deseas actualizar: ")
    if palabra in diccionario:
        nueva_definicion = input(f"Introduce la nueva definición de '{palabra}': ")
        diccionario[palabra] = nueva_definicion
        print(f'Definición de "{palabra}" actualizada a: "{nueva_definicion}"')
    else:
        print(f'La palabra "{palabra}" no se encuentra en el diccionario.')
        i = input("Desea agregar esa nueva palabra? si/no  ")
        if i == "si":
            agregar_palabra(diccionario)
        else:
            print("el diccionario no se ha modificado...")
            
def mostrar_diccionario(diccionario):
    print(diccionario)
    
              

archivo_diccionario = 'diccionario.json'

diccionario = cargar_diccionario(archivo_diccionario)

while True:
    print("\n1. Agregar nueva palabra")
    print("2. Buscar palabra")
    print("3. Actualizar palabra")
    print("4. Mostrar diccionario")
    print("5. Guardar y salir")
    
    opcion = input("Elige una opción: ").strip()
    
    if opcion == '1':
        agregar_palabra(diccionario)
    elif opcion == '2':
        buscar_palabra(diccionario)
    elif opcion == '3':
        actualizar_palabra(diccionario)
    elif opcion == "4":
        mostrar_diccionario(diccionario)
    elif opcion == '5':
        guardar_diccionario(diccionario, archivo_diccionario)
        print("Diccionario guardado. ¡Hasta luego!")
        break
    else:
        print("Opción no válida, por favor elige una opción del 1 al 4.")
