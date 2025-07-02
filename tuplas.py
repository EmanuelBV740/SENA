# tupla=(1,2,3,4,)
# lista=list(tupla)
# print (f"{lista}")

# lista2=[1,1,1,1]
# tupla2=tuple(lista)
# print (f"{tupla}")

# Ejercicio 1
frutas = ("manzana", "pera")
lista_frutas = list(frutas)
nueva_fruta = input("Ingresa una nueva fruta: ")
lista_frutas.append(nueva_fruta)
frutas = tuple(lista_frutas)
print("Tupla final de frutas:", frutas)


# Ejercicio 2
calificaciones = (4.2, 3.8)
lista_calificaciones = list(calificaciones)
nueva_nota = float(input("Ingresa una nueva calificación: "))
lista_calificaciones.append(nueva_nota)
calificaciones = tuple(lista_calificaciones)
print("Calificaciones finales:", calificaciones)


# Ejercicio 3
datos = ("Ana", "Gómez")
lista_datos = list(datos)
documento = input("Ingresa el número de documento: ")
lista_datos.append(documento)
datos = tuple(lista_datos)
print("Datos personales completos:", datos)





