# Codifica un programa en Python que nos permita guardar los nombres de los alumnos de una clase
# y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la
# información en un diccionario cuyas claves serán los nombres de los alumnos y los valores serán
# listas con las notas de cada alumno.
# El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo
# sus notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista
# de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un
# alumno que ya existe el programa nos dará un error.

alumnos = {}
cantidad = int(input("Introduce la cantidad de alumnos: "))
for num in range(cantidad):
    alumno = input("Nombre del alumno: ")
    if alumno in alumnos:
        print("Alumno ya existe.")
        alumno = input("Nombre del alumno :")
    notas=[]
    nota = int(input("Dame una nota del alumno: "))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Dame una nota del alumno: "))
        suma = 0
        for i in notas:
            suma += i
        long = len(notas)
        notasT = suma/long
        
        alumnos[alumno] = notasT

print(alumnos)