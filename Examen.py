matriz = [
    [73, 12, 89, 34],
    [5, 61, 27, 94],
    [46, 18, 80, 3]
]

matriz.append([39, 22, 69, 17])
print(matriz)

print(matriz[1])

for i in matriz:
    if 18 in i:
        print(f"18 encontrado en la fila {i}")
        break


for filas in matriz:
    for numeros in filas:
        if numeros == 61:
            print(f"61 encontrado en {filas}")
            break

numeros = [10, 20, 30, 40, 50]
print(numeros)
numeros.append([60,70])
print(numeros [5])
numeros.insert(1,15)
print (numeros)