alumnos = []

# Ingresar datos de los alumnos
while True:
  nombre = input("Ingrese el nombre del alumno: ")
  notas = []
  for i in range(1, 4):
    nota = int(input("Ingrese la nota {}: ".format(i)))
    notas.append(nota)

  alumno = {"Alumno": nombre, "Notas": notas}
  alumnos.append(alumno)

  respuesta = input("¿Desea registrar otro alumno? (SI/NO): ").upper()
  if respuesta == "NO":
    break

# Mostrar listado de alumnos
for alumno in alumnos:
  print("**Alumno:**", alumno["Alumno"])
  print("**Notas:**", alumno["Notas"])
  print()