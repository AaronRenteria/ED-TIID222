
#Declaramos nuestro arreglo
numeros = [10,20,30,40,50]

print(numeros[2])

numeros[2] = 100
print(numeros)

numeros.append(60)
print(numeros)

numeros.append([60,70])
numeros.append(60)
numeros.append(70)

numeros = numeros + [60] + [70] + [80]
print (numeros)

num = [10,20,30]
otros_numeros = [40,50,60]
num.extend(otros_numeros)
print(num)

len(numeros)

numeros[len(numeros):]
numeros[3:]


nume = [10,20,30]
nume[len(nume):] = [40]
print(nume)


print("EJERCICIO 1")
calificaciones = [70, 85, 90, 65]

# Agregar 95 al final
calificaciones.append(95)
print(calificaciones)

# Agregar 80 entre 85 y 90
calificaciones.insert(2, 80)
print(calificaciones)

# Imprimir arreglo completo
print(calificaciones)


print("EJERCICIO 2")
colores = ["Azul", "Amarillo", "Rosa"]

colores.extend(["Verde", "Morado", "Rojo"])

print(colores)

print("Negro")


print("EJERCICIO 3")

numeros = [10, 20, 30, 40]

# Agregar 95 entre 20 y 30
numeros.insert(2, 95)

# Agregar 50 y 67 al final
numeros.append(50)
numeros.append(67)

# Imprimir arreglo completo
print(numeros)

# Imprimir 95
print(numeros[2])

# Imprimir 67
print(numeros[6])