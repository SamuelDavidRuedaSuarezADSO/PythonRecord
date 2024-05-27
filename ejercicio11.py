# Realizar un algoritmo el cual sume los ingresos de una empresa mensualmente, teniendo en
# cuenta que se debe saber de que son las ganancias y se debe pedir al usuario de cuanto dinero
# total se obtuvo de esa ganancia, al final se deberá saber si las ganancias son mayores a las
# ganancias del año pasado, entonces imprimir en pantalla que se obtuvieron mas ganancias y hacer
# la respectiva operación para saber de cuanta diferencia fue la ganancia, si las ganancias son
# menores a las ganancias del año pasado imprimir en pantalla el faltante de ganancias para
# completar las ganancias del año pasado. GANANCIAS: Pedir al usuario que ingrese las ganancias
# del año pasado.

gananciasPasado = float(input("Ingrese las ganancias del año pasado: "))

gananciasActual = 0
gananciasMensuales = []

for mes in range(1,12):
    gananciasMes = float(input(f"Ingrese las ganancias del mes {mes}: "))
    gananciasMensuales.append(gananciasMes)
    gananciasActual += gananciasMes
if gananciasActual > gananciasPasado:
    diferencia = gananciasActual - gananciasPasado
    print("\nSe obtuvieron más ganancias este año que el año pasado")
    print(f"Diferencia de ganancias respecto al año pasado y este año es de {diferencia}")
elif gananciasActual < gananciasPasado:
    diferencia = gananciasPasado - gananciasActual
    print("\nSe obtuvieron menos ganancias este año que el año pasado")
    print(f"Faltante de ganancias para alcanzar las del año pasado: {diferencia}")
else:
    print("\nLas ganancias de este año son iguales a las del año pasado.")


print(f"\nGanancias totales del año actual: {gananciasActual}")