# Crear un programa en Python donde se le pregunte al usuario su nombre su edad y su número de
# documento, todo esto deberá estar almacenado en un diccionario.

nom= input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
docum = int(input("Ingrese su numero de documento: "))

usuario={
  "nombre": nom,
  "edad": edad,
  "documento": docum
}
print("Usuario añadido")
print(usuario)