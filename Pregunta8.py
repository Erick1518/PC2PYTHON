def factorial(numero):

  if numero < 0:
    raise ValueError("El número debe ser un entero no negativo")
  elif numero == 0 or numero == 1:
    return 1
  else:
    factorial = 1
    for i in range(2, numero + 1):
      factorial *= i
    return factorial

# Ejemplo
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")