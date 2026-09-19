""" numeros = [10,20,30,40,50]

print(numeros[2])

numeros[3] = 15
print(numeros)

numeros.append(60)
print(numeros)

numeros.pop(1)
print(numeros)

frutas = ["manzana", "pera", "naranja", "kiwi"]
frutas.remove("manzana") 
print(frutas)   


frutas.pop(3)
print(frutas)

frutas.append("sandia")
print(frutas)

frutas[1] = "fresa"
print(frutas) """



arreglos = []
n = int(input("Ingrese el tamaño del arreglo: "))
for i in range(n):
    arreglos.append(int(input("Ingrese un número: ")))
print(arreglos)
