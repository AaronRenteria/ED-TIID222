# Declarando un arreglo

numeros = [10, 20, 30, 40, 50]

# Imprimimos un elemento específico del arreglo

print(numeros[2])

# Reasignamos un valor específico del arreglo

numeros[3] = 35

print(numeros)

# Agregamos un nuevo valor al final del arreglo

numeros.append(60)

print(numeros)

# Eliminamos un valor del arreglo

numeros.remove(35)

print(numeros)

# Eliminamos un valor del arreglo usando la posición

numeros.pop(4)

print(numeros)


# Arreglo de frutas

frutas = ["Manzana", "Fresa", "Sandia", "Mango", "Melon", "Platano"]

# Eliminamos un elemento usando su posición

frutas.pop(4)

print(frutas)

# Eliminamos un elemento del arreglo usando su nombre

frutas.remove("Manzana")

print(frutas)


# Declaramos un arreglo vacío

arreglo = []

print(arreglo)

# Creamos una variable para saber de qué tamaño queremos el arreglo

n = int(input("Ingrese el tamaño del arreglo: "))

print(n)

# Se hace un ciclo para llenar el arreglo usando append

for i in range(n):
    dato = int(input("Ingrese un número: "))
    arreglo.append(dato)

print(arreglo)


# Ahora no se utiliza append

n = int(input("Ingrese el tamaño del arreglo: "))

# Creamos el arreglo con el tamaño indicado

arreglo = [0] * n

# Se hace un ciclo para llenar cada posición del arreglo

for i in range(n):
    dato = int(input("Ingrese un número: "))
    arreglo[i] = dato

print(arreglo)

#Enunciado: Escribe un programa que rellene un array de 15 elementos con números enteros comprendidos entre 0 y 500 (pedir números).
#  A continuación, se mostrará el array “Cincuerizado”, según el siguiente criterio: si el número que hay en una posición del array 
# es múltiplo de 5, se deja igual y, si no, se cambia por el siguiente múltiplo de 5 que exista a partir de él.


# Declaramos un arreglo vacío

arreglo = []

# Pedimos 15 números

for i in range(15):
    dato = int(input("Ingrese un número entre 0 y 500: "))
    arreglo.append(dato)

print("Array original:")
print(arreglo)


for i in range(15):

    # Si NO es múltiplo de 5
    if arreglo[i] % 5 != 0:

        # Buscamos el siguiente múltiplo de 5
        arreglo[i] = arreglo[i] + (5 - arreglo[i] % 5)

print("Array cincuerizado:")
print(arreglo)