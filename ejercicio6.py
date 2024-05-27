# En una escuela se necesita un programa el cual gestione la cantidad de personas que entran a
# cuyo salón, teniendo en cuenta que se debe que tener la información personal de cada estudiante
# y de los profesores, así mismo, se debe tener un registro del número del salón al cual se le valla a
# hacer la gestión y que al final se muestre en pantalla

verdad = True
numS = int(input("Ingresa el numero del salón: "))

alumnos ={}
profesor ={}

sumaAlumn =0
sumaProfe =0
sumaTotal =0

while (verdad):
  quest = (input("¿Eres un alumno?: (Si/No) "))
  if quest == "si":
    nif = int(input("Ingresa el documento: "))
    nom = input("Ingresa el nombre: ")
    telef = int(input("Ingrese su numero telefonico: "))
    direcc = input("Ingrese la direccion: ")

    alum = {
      "nombre": nom,
      "telefono": telef,
      "direccion": direcc,
    }
    alumnos[nif]= alum
    sumaAlumn += 1
    sumaTotal += 1

  elif quest == "no":
    nif = int(input("Ingrese el documento: "))
    nomb = input("Ingresa el nombre: ")
    telefo = int(input("Ingrese su numero telefonico: "))
    direcci = input("Ingrese la direccion: ")

    profe ={
      "nombre": nomb,
      "telefono": telefo,
      "direccion": direcci,
    }
    profesor[nif]=profe
    sumaProfe +=1
    sumaTotal +=1

  else:
    print("Error: Opcion no valida")

  opc = input("¿Desea terminar el ingreso de datos?: (Si/No) ")
  if opc == "si":
    verdad = False
    print("En el salon ", numS)
    print("Hay un total de ",sumaTotal, " personas")
    print("Hay un total de ",sumaProfe, " profesores")
    print("Hay un total de ",sumaAlumn, " alumnos ")
    print("Alumnos: ", alumnos)
    print("Profesores: ", profesor)