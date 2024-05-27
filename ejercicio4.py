
# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los
# clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor
# será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
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
# • Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.1
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
    "preferente": True
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

match (opc):
  case 1:
    nif = input("Ingresa el NIF: ")
    nom = input("Ingresa el nombre: ")
    direcc = input("Ingrese la direccion: ")
    telefono = int(input("Ingresa el telefono: "))
    correo = input("Ingresa el correo: ")
    preferente = input("¿Es un cliente preferenta?: ")
    if preferente == "si":
      preferente = True
    else:
      preferente = False
    cliente = {
      "nombre": nom,
      "direccion": direcc,
      "telefono": telefono,
      "correo": correo,
      "preferente": preferente,
    }
    clientes[nif]=cliente
    
    print("Cliente Agregado correctamente"),
  case 2:
    print(clientes)
    print("¿Que cliente desea eliminar? Ingresa el NIF")
    eli = int(input())
    if eli in clientes:
      clientes.pop(eli)
      print("Cliente elimado")
      print(clientes)
    else:
      print("Error: No se elimino")
  case 3:
    print(clientes)
    print("¿Que cliente desea mostrar?: ")
    most = int(input())

    if most in clientes:
      print(clientes[most])
    else:
      print("Error: No se encontro ese cliente")
  case 4:
    print(clientes)
  case 5:
     for nif, cliente in clientes.items():
        if cliente["preferente"]:
            print("NIF:", nif, "- Nombre:", cliente["nombre"])
  case 6:
    print("¡¡Hasta luego!!"),