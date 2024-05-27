# Escribe un programa Python que pida un número por teclado y que cree un diccionario cuyas claves
# sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

num = int(input("Ingrese el numero deseado: "))
dicc={}
for i in range(1,num+1):
  dicc.setdefault(i, i**2),

print(dicc)
