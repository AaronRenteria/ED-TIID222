
pila = []

while True:
    print("\n--- MENU DE PILAS ---")
    print("1. Insertar pila")
    print("2. Borrar en pila")
    print("3. Listar pila")
    print("4. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        numero = int(input("Ingresa un numero: "))
        pila.append(numero)
        print("Numero agregado correctamente.")

    elif opcion == "2":
        if len(pila) > 0:
            eliminado = pila.pop()
            print("Elemento eliminado:", eliminado)
        else:
            print("La pila esta vacia.")

    elif opcion == "3":
        print("Pila actual:", pila)

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opcion no valida.")

    nuevamente = input("Deseas ejecutar nuevamente? (s/n): ")

    if nuevamente.lower() != "s":
        break

print("Programa terminado.")

