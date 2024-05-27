# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en
# un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive
# en <dirección> y su número de teléfono es <teléfono>.

diccionario = {
  "nombre": input("Ingrese el nombre: "),
  "edad": input("Ingrese la edad: "),
  "direcc": input("Ingrese la direccion: "),
  "telefe": input("Ingrese el telefono: ")
}

print(f"{diccionario.get('nombre')} tiene {diccionario.get('edad')} años, vive en {diccionario.get('direcc')} y su telefono es {diccionario.get('telefe')}")