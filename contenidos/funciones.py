# Funciones matemáticas
print(abs(-5))  # Valor absoluto. Imprime: 5
print(max(1, 2, 3))  # Máximo de los argumentos. Imprime: 3
print(min(1, 2, 3))  # Mínimo de los argumentos. Imprime: 1
print(pow(2, 3))  # Potencia (2 elevado a 3). Imprime: 8
print(round(3.14159, 2))  # Redondeo. Imprime: 3.14

# Funciones de conversión de tipo
print(int("123"))  # Convierte una cadena a un entero. Imprime: 123
print(float("3.14159"))  # Convierte una cadena a un flotante. Imprime: 3.14159
print(str(123))  # Convierte un número a una cadena. Imprime: "123"

# Funciones de colecciones
lista = [1, 2, 3, 4, 5]
print(len(lista))  # Longitud de la lista. Imprime: 5
print(sum(lista))  # Suma de los elementos de la lista. Imprime: 15
print(sorted(lista, reverse=True))  # Ordena la lista en orden inverso. Imprime: [5, 4, 3, 2, 1]

# Otras funciones
print(type(123))  # Tipo de un valor. Imprime: <class 'int'>
print(isinstance(123, int))  # Comprueba si un valor es de un cierto tipo. Imprime: True