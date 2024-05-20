# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en
# un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive
# en <dirección> y su número de teléfono es <teléfono>.


# diccionario = {
#   "nombre": input("Ingrese el nombre: "),
#   "edad": input("Ingrese la edad: "),
#   "direcc": input("Ingrese la direccion: "),
#   "telefe": input("Ingrese el telefono: ")
# }

# print(f"{diccionario.get('nombre')} tiene {diccionario.get('edad')} años, vive en {diccionario.get('direcc')} y su telefono es {diccionario.get('telefe')}")


# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al
# usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos
# de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello

# dicc = {
#   "platano": 1.35,
#   "manzana": 0.80,
#   "pera": 0.85,
#   "naranja": 0.70
# }

# fruta = input("Ingrese el nombre de la fruta que deseea: ")
# kilos = float(input("Ingrese los kilos de fruta que desea: "))

# if fruta in dicc :
#   press = dicc.get(fruta)
#   total = press*kilos
#   print(f"Su total de compra es de ${total}")
# else:
#   print("No existe esa fruta")


# Escribe un programa Python que pida un número por teclado y que cree un diccionario cuyas claves
# sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

# num = int(input("Ingrese el numero deseado: "))

# dicc={}

# for i in range(1,num+1):
#   dicc.setdefault(i, i**2),

# print(dicc)


# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los
# clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor
# será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
# GFPI-F-135 V02
# donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe
# preguntar al usuario por una opción del siguiente menú:
# (1) Añadir cliente,
# (2) Eliminar cliente,
# (3) Mostrar cliente,
# (4) Listar todos los clientes,
# (5) Listar clientes preferentes,
# (6) Terminar.
#  En función de la opción elegida el programa tendrá que hacer lo siguiente:
# • Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# • Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# • Preguntar por el NIF del cliente y mostrar sus datos.
# • Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# • Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.

clientes ={
  1100: {
    "nombre": "Juan",
    "direccion": "calle 20",
    "telefono": 310326,
    "correo": "juan85@soy.sena",
    "preferente": False
  },
  1101: {
    "nombre": "Jose",
    "direccion": "calle 2A",
    "telefono": 310422,
    "correo": "josepuello@gmail.com",
    "preferente": False
  },
  1102: {
    "nombre": "Samuel",
    "direccion": "calle 48",
    "telefono": 301210,
    "correo": "sampuerta@gmail.ocom",
    "preferente": True
  }
}

print("¿Que desea hacer?: ")

opc = int(input("(1) Añadir Cliente\n(2) Eliminar Cliente\n(3) Mostrar Cliente\n(4) Listar todos los Clientes\n(5) Listar Clientes Preferentes\n(6) Terminar\n"))