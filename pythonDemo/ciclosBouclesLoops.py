# Ciclo for
for i in range(5):
    print(i)  # Imprime los números del 0 al 4

# Ciclo while
i = 0
while i < 5:
    print(i)  # Imprime los números del 0 al 4
    i += 1

# Comprensión de listas
lista = [i for i in range(5)]  # Crea una lista con los números del 0 al 4
print(lista)  # Imprime: [0, 1, 2, 3, 4]

# Ciclo for con una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)  # Imprime: manzana, banana, cereza

# Ciclo for con una cadena
for letra in "hola":
    print(letra)  # Imprime: h, o, l, a

# Ciclo for con un diccionario
diccionario = {"nombre": "Juan", "edad": 30}
for clave, valor in diccionario.items():
    print(clave, valor)  # Imprime: nombre Juan, edad 30