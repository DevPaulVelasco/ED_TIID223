from collections import deque

cola = deque(["Ana", "Carlos"])

cola.append("Jorge")
cola.append("Manuel")
print("Cola actual:", cola)

atendido = cola.popleft()
print(f"Se atendio a: (atendido)")
print ("Cola restante" , cola)
atendido = cola.popleft()
print(f"Se atendio a: (atendido)")
print ("Cola restante" , cola)
#hola