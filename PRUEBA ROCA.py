import os
os.system ("cls")
numeros = []

for i in range(3):
    numero = int(input(f"Ingrese el número {i+1}: "))
    if numero <= 0:
        print("no es mayor a 0")
    numeros.append(numero) 
print(numeros)

os.system("pause")
os.system("cls")

for numero in numeros[:]:  
    if numero <= 0:
        numeros.remove(numero) 
        print(f"El número {numero} ha sido eliminado por ser menor")
        
numeros.sort()

intervalo_completo = []

for i in range(len(numeros) - 1):
    intervalo_completo.append(numeros[i])
    
    for j in range(int(numeros[i]) + 1, int(numeros[i + 1])):
        intervalo_completo.append(j)

if numeros:
    intervalo_completo.append(numeros[-1])

intervalo_completo.sort(reverse=True)
print(intervalo_completo)