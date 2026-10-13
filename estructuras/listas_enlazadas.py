class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def buscar(self, dato):
        actual = self.cabeza
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def eliminar(self, dato):
        if self.cabeza is None:
            return False

        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return True

        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                return True
            actual = actual.siguiente

        return False

    def mostrar(self):
        elementos = []
        actual = self.cabeza

        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente

        print(" -> ".join(elementos) if elementos else "Lista vacia")


if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.agregar(10)
    lista.agregar(20)
    lista.agregar(30)

    print("Lista:")
    lista.mostrar()

    print("¿Esta el 20 en la lista?", lista.buscar(20))
    lista.eliminar(20)

    print("Lista despues de eliminar el 20:")
    lista.mostrar()