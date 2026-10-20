def ejecutar_programa():
    pila = []

    while True:
        print("\n--- MENÚ DE PILAS ---")
        print("1. Insertar en pila")
        print("2. Borrar en pila")
        print("3. Listar pila")
        print("4. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            try:
                numero = int(input("Ingresa un número entero: "))
                pila.append(numero)
                print(f"Se agregó {numero} a la cima de la pila.")
            except ValueError:
                print("Entrada inválida. Debes ingresar un número entero.")

        elif opcion == "2":
            if pila:
                eliminado = pila.pop()
                print(f"Se eliminó el último elemento agregado: {eliminado}")
            else:
                print("La pila está vacía; no hay elementos que eliminar.")

        elif opcion == "3":
            if pila:
                print("Elementos de la pila (base → cima):")
                print(pila)
            else:
                print("La pila está vacía.")

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