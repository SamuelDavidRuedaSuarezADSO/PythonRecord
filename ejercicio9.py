# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada
# mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada
# mes

año = 12
suma= 0
for mes in range(año):
  m = int(input(f"Ingresa lo ahorrado del {mes+1} mes: "))
  suma += m
  print(f"has ahorrado {suma}")