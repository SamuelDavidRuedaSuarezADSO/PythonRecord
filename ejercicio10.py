# 10. Conozca si tiene que declarar el impuesto de renta desde el próximo año, según sus ingresos
# mensuales, si sus ingresos mensuales son mayores de 3.000.000 se le deberá cobrar 250.000 más
# la implementación de un IVA del 18% de los ingresos mensuales, si los ingresos mensuales son
# menores a 3.000.000 se le cobrara 200.000 más la implementación del IVA aproximadamente del
# 10% de sus ingresos mensuales.

ingre = int(input("Ingrese sus ingresos: "))

if ingre >= 3000000:
  x = ingre*0.18
  cobro = 250000 + x

elif ingre >0 and ingre < 3000000:
  x = ingre*0.10
  cobro = 200000 + x

print("Tienes que pagar: ", cobro)