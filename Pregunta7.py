def es_primo(numero):
 
  if numero <= 1:
    return False
  elif numero <= 3:
    return True
  elif numero % 2 == 0 or numero % 3 == 0:
    return False
  i = 5
  while i * i <= numero:
    if numero % i == 0 or numero % (i + 2) == 0:
      return False
    i += 6
  return True

# Ejemplo
numero = 11
if es_primo(numero):
  print(f"El número {numero} es primo")
else:
  print(f"El número {numero} no es primo")