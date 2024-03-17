# función calcula el n-ésimo número de Fibonacci.
def fibonacci(n):
  
  if n == 0 or n == 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

# Imprimir la serie de Fibonacci entre 0 y 50
for i in range(51):
  print(fibonacci(i))