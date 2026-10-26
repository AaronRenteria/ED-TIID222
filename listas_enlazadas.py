class Nodo:
    def __init__(self, numero):
        # Estructura de un nodo [numero] [referencia]
        self.numero = numero
        self.siguiente = None


# Clase que va a administrar todos los nodos de la lista enlazada
class ListEnlazda:
    def __init__(self):
        self.cabeza = None

    # Metodo para insertar un nodo al inicio de la lista
    def Insertar_Nodo_al_Inicio(self, numero):
        # Crear un nuevo nodo con el numero recibido
        nuevo_nodo = Nodo(numero)

        # Comprobamos si la lista esta vacia
        if self.cabeza is None:
            # El nuevo nodo sera la cabeza
            self.cabeza = nuevo_nodo
            return

        # El nuevo nodo apunta al que era la cabeza
        nuevo_nodo.siguiente = self.cabeza

        # Actualizamos la cabeza
        self.cabeza = nuevo_nodo

    # Metodo para insertar un nodo al final de la lista
    def Insertar_Nodo_al_Final(self, numero):
        # Crear el nodo con el numero que recibe
        nuevo_nodo = Nodo(numero)

        # Comprobar si la lista esta vacia
        if self.cabeza is None:
            # El nuevo nodo sera el primero
            self.cabeza = nuevo_nodo
            return

        # Referencia temporal al primer nodo
        actual = self.cabeza

        # Recorrer la lista hasta llegar al ultimo nodo
        while actual.siguiente:
            actual = actual.siguiente

        # El ultimo nodo apunta al nuevo nodo
        actual.siguiente = nuevo_nodo

    # Metodo para imprimir nuestra lista enlazada
    def Imprimir_listaEnlazada(self):
        actual = self.cabeza

        while actual:
            # Imprimir los numeros sin saltos de linea
            print(actual.numero, "→", end=" ")

            # Avanzar al siguiente nodo
            actual = actual.siguiente

        print("None")


# Crear nuestra lista
Mi_Lista = ListEnlazda()

# Insertar nodos al inicio
Mi_Lista.Insertar_Nodo_al_Inicio(2)
Mi_Lista.Insertar_Nodo_al_Inicio(1)

# Insertar nodo al final
Mi_Lista.Insertar_Nodo_al_Final(56)

# Imprimir la lista enlazada
Mi_Lista.Imprimir_listaEnlazada()