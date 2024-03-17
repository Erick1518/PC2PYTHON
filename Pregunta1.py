# Función para verificar si un número es divisible por 7 y múltiplo de 5
def divisible_por_7_y_5(numero):
  return numero % 7 == 0 and numero % 5 == 0

# Rango de números a analizar
numeros = range(1500, 2701)

# Lista para almacenar los números encontrados
numeros_encontrados = []

# Recorrer el rango de números
for numero in numeros:
  
  # Verificar si el número es divisible por 7 y múltiplo de 5
  if divisible_por_7_y_5(numero):
    
    # Agregar el número a la lista
    numeros_encontrados.append(numero)

# Imprimir los números encontrados
if numeros_encontrados:
  print("Números divisibles por 7 y múltiplos de 5 en el rango:", numeros_encontrados)
else:
  print("No se encontraron números divisibles por 7 y múltiplos de 5 en el rango.")