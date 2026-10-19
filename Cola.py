
cola = []

while True:
    print("\n--- MENU DE COLAS ---")
    print("1. Insertar cola")
    print("2. Borrar en cola")
    print("3. Listar cola")
    print("4. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        numero = int(input("Ingresa un numero: "))
        cola.append(numero)
        print("Numero agregado correctamente.")

    elif opcion == "2":
        if len(cola) > 0:
            eliminado = cola.pop(0)
            print("Elemento eliminado:", eliminado)
        else:
            print("La cola esta vacia.")

    elif opcion == "3":
        print("Cola actual:", cola)

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opcion no valida.")

    nuevamente = input("Deseas ejecutar nuevamente? (s/n): ")

    if nuevamente.lower() != "s":
        break

print("Programa terminado.")
