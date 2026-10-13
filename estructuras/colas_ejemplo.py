matriz = [
    [12,34,12]
    [23,45,12]
    [54,65,23]
]

for i in matriz:
    if 80 in i:
        print(f"el 80 esta en la fila (i)")
        break
    for fila in matriz:
        for numero in fila:
            if numero == 80:
                print(f"El 80 esta en (fila)")