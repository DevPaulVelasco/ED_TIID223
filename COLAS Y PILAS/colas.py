from collections import deque


def ejecutar_programa():
    cola = deque()

    while True:
        print("\n--- MENÚ DE COLAS ---")
        print("1. Insertar en cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            try:
                numero = int(input("Ingresa un número entero: "))
                cola.append(numero)
                print(f"Se agregó {numero} al final de la cola.")
            except ValueError:
                print("Entrada inválida. Debes ingresar un número entero.")

        elif opcion == "2":
            if cola:
                eliminado = cola.popleft()
                print(f"Se eliminó el primer elemento: {eliminado}")
            else:
                print("La cola está vacía; no hay elementos que eliminar.")

        elif opcion == "3":
            if cola:
                print("Elementos de la cola (primero en salir → último):")
                print(list(cola))
            else:
                print("La cola está vacía.")

        elif opcion == "4":
            print("Has elegido salir.")
            break

        else:
            print("Opción no válida. Selecciona una opción del 1 al 4.")


while True:
    ejecutar_programa()
    respuesta = input("\n¿Deseas ejecutar nuevamente el programa? (s/n): ").strip().lower()
    if respuesta != "s":
        print("Programa finalizado.")
        break
