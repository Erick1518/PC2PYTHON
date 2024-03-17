def contar_digito(numero, digito):
  numero_str = str(numero)
  return numero_str.count(str(digito))

# Ejemplo de uso
numero = 15789000
digito = 0
cantidad = contar_digito(numero, digito)

# La cantidad de veces que el dígito aparece en el número.
print(f"Cantidad de veces {digito} en el número {numero}: {cantidad}")