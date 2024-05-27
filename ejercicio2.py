# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al
# usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos
# de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello

dicc = {
  "platano": 1.35,
  "manzana": 0.80,
  "pera": 0.85,
  "naranja": 0.70
}

fruta = input("Ingrese el nombre de la fruta que deseea: ")
kilos = float(input("Ingrese los kilos de fruta que desea: "))

if fruta in dicc :
  press = dicc.get(fruta)
  total = press*kilos
  print(f"Su total de compra es de ${total}")
else:
  print("No existe esa fruta")