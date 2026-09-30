from collections import deque
import time

cola = deque()

cola.append("Ana")
cola.append("Carlos")
cola.append("Elena")

print("Cola actual: ",list(cola))

time.sleep(2)
atendido = cola.popleft()
print("Se atendio a:", atendido)

time.sleep(2)

print("Siguiente en la fila: ",cola[0])

time.sleep(3)

print("Cola restante:",list(cola))
matriz = [
    [1,2],
    [3,4]
]

matriz.append([5,6])

print(matriz[0][1])

matriz[0][1] = 10

if 3 in matriz[1]:
    print("Encontrado")


matriz[0].append(7)
matriz[1].append(8)
matriz[2].append(9)

print(matriz)