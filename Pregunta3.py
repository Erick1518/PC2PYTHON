numeros = []

while True:
  respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()
  if respuesta == "NO":
    break
  else:
    numero = int(input("Ingrese el número: "))
    numeros.append(numero)

# Contar pares e impares
pares = 0
impares = 0
for numero in numeros:
  if numero % 2 == 0:
    pares += 1
  else:
    impares += 1

# Mostrar resultados
print("Números ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)