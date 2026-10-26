
from collections import deque

cola = deque()

while True:
    print("\n--- MENU DE COLAS ---")
    print("1. Insertar en cola")
    print("2. Borrar en cola")
    print("3. Listar cola")
    print("4. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        numero = int(input("Ingresa un numero: "))
        cola.append(numero)
        print("Numero agregado.")

    elif opcion == "2":
        if len(cola) > 0:
            print("Elemento eliminado:", cola.popleft())
        else:
            print("La cola esta vacia.")

    elif opcion == "3":
        print("Cola actual:", list(cola))

    elif opcion == "4":
        break

    else:
        print("Opcion no valida.")

    nuevamente = input("Deseas ejecutar nuevamente? (s/n): ")
    if nuevamente.lower() != "s":
        break

print("Programa terminado.")
