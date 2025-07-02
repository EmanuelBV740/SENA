print("Listas, Tuplas, Diccionarios y Operaciones")
print("punto 1")
print("Calculadora")
calificacion_uno=float(input("Ingrese la calificacion uno: "))
calificacion_dos=float(input("Ingrese la calificacion dos: "))
calificacion_tres=float(input("Ingrese la calificacion tres: "))
calificaciones=[calificacion_uno,calificacion_dos,calificacion_tres]
calificaciones_promedio=sum(calificaciones)/len(calificaciones)
print(f"El promedio de las notas ingresadas es: {calificaciones_promedio}")

print("Punto 2")
print("Actualiza precios")
productos={"leche":2000,"huevos":17500,"arina":5000}
print(f"Los productos y sus precios son:\n{productos}")
porcentaje_uno=int(input("Ingrese el procentaje a aumentar de la leche: "))
porcentaje_dos=int(input("Ingrese el procentaje a aumentar de los huevos: "))
porcentaje_tres=int(input("Ingrese el procentaje a aumentar de la arina: "))
productos["leche"]=productos["leche"]+((productos["leche"]*porcentaje_uno)/100)
productos["huevos"]=productos["huevos"]+((productos["huevos"]*porcentaje_uno)/100)
productos["arina"]=productos["arina"]+((productos["arina"]*porcentaje_uno)/100)
print(f"Los productos con sus precios aumentados son:\n{productos}")

print("Punto 3")
print("Conversor de temperaturas")
celsius_dia_uno=float(input("Ingrese la temperatura en Celsius del dia uno: "))
celsius_dia_dos=float(input("Ingrese la temperatura en Celsius del dia dos: "))
celsius_dia_tres=float(input("Ingrese la temperatura en Celsius del dia tres: "))
celsius_dia_cuatro=float(input("Ingrese la temperatura en Celsius del dia cuatro: "))
celsius_dia_cinco=float(input("Ingrese la temperatura en Celsius del dia cinco: "))
temperaturas_celsius=(celsius_dia_uno,celsius_dia_dos,celsius_dia_tres,celsius_dia_cuatro,celsius_dia_cinco)
print(f"Las temperaturas en celsius que ingreso son: \n{temperaturas_celsius}")
fahrenheit_dia_uno=celsius_dia_uno*(9/5)+32
fahrenheit_dia_dos=celsius_dia_dos*(9/5)+32
fahrenheit_dia_tres=celsius_dia_tres*(9/5)+32
fahrenheit_dia_cuatro=celsius_dia_cuatro*(9/5)+32
fahrenheit_dia_cinco=celsius_dia_cinco*(9/5)+32
temperaturas_fahrenheit=(fahrenheit_dia_uno,fahrenheit_dia_dos,fahrenheit_dia_tres,fahrenheit_dia_cuatro,fahrenheit_dia_cinco)
print(f"Las temperaturas que ingreso en fahrenheit son: \n{temperaturas_fahrenheit}")

print("punto 4")
print("Edad promedio con listas")
edad_uno=int(input("Ingrese la edad uno: "))
edad_dos=int(input("Ingrese la edad dos: "))
edad_tres=int(input("Ingrese la edad tres: "))
edad_cuatro=int(input("Ingrese la edad cuatro: "))
edad_cinco=int(input("Ingrese la edad cinco: "))
edades=[edad_uno,edad_dos,edad_tres,edad_cuatro,edad_cinco]
print(f"Las edades son: {edades}\nLa edad mayor es: {max(edades)}\nLa edad menor es: {min(edades)}\nEl promedio de las edades es: {sum(edades)/len(edades)}")

print("Punto 5")
print("Diccionario de frutas")
frutas={"manzana":7521,"pera":1926,"guayaba":2580}
print(f"las frutas con su precio por Kilo son:\n{frutas}")
kilos_manzana=int(input("Cuantos kilos desea de manzana: "))
kilos_pera=int(input("Cuantos kilos desea de pera: "))
kilos_guayaba=int(input("Cuantos kilos desea de guayaba: "))
precio_manzana=frutas["manzana"]*kilos_manzana
precio_pera=frutas["pera"]*kilos_pera
precio_guayaba=frutas["guayaba"]*kilos_guayaba
total_pagar=precio_manzana+precio_pera+precio_guayaba
print(f"El total a pagar por la cantidad de frutas compradas es de: {total_pagar}$")

print("Punto 6")
print("Suma de elementos en tupla")
numeros=(45,17,4,90,3)
print(f"Los numeros en la tupla son: {numeros}\nLa suma de sus elementos es: {sum(numeros)}")

print("Punto 7")
print("Inventario con lista de diccionarios")
producto_uno={}
producto_uno["nombre"]=input("Ingrese el nombre del producto uno: ")
producto_uno["cantidad"]=int(input("Ingrese la cantidad del producto uno: "))
producto_uno["precio"]=float(input("Ingrese el precio del producto uno: "))
producto_dos={}
producto_dos["nombre"]=input("Ingrese el nombre del producto dos: ")
producto_dos["cantidad"]=int(input("Ingrese la cantidad del producto dos: "))
producto_dos["precio"]=float(input("Ingrese el precio del producto dos: "))
producto_tres={}
producto_tres["nombre"]=input("Ingrese el nombre del producto tres: ")
producto_tres["cantidad"]=int(input("Ingrese la cantidad del producto tres: "))
producto_tres["precio"]=float(input("Ingrese el precio del producto tres: "))
inventario_productos=[producto_uno,producto_dos,producto_tres]
print(f"Estas son los productos disponibles en el inventario: {inventario_productos}")

print("Punto 8")
print("Modificar una lista de precios")
precios=[5000,2800,18000,10000,954000]
print(f"Estos son los precios actuales: {precios}")
porcetaje=int(input("Ingrese el porcentaje de descuento que se le va a aplicar a los precios: "))
precios[0]=precios[0]-((precios[0]*porcetaje)/100)
precios[1]=precios[1]-((precios[1]*porcetaje)/100)
precios[2]=precios[2]-((precios[2]*porcetaje)/100)
precios[3]=precios[3]-((precios[3]*porcetaje)/100)
precios[4]=precios[4]-((precios[4]*porcetaje)/100)
print(f"Los precios con el descuento aplicado son: {precios}")

print("Punto 9")
print("Nota con tuplas")
notas=(float(input("Ingrese la nota uno: ")),float(input("Ingrese la nota dos: ")),float(input("Ingrese la nota tres: ")),float(input("Ingrese la nota cuatro: ")))
print(f"Las notas ingresadas son: {notas}\nLa nota mas baja ingresada es {min(notas)}\nLa nota mas alta ingresada es: {max(notas)}")

print("Punto 10")
print("Diccionario de conversiones")
unidades_metros={"km":1000,"m":1,"cm":0.01}
unidades=input("Ingrese la unidad a convertia a metros (km, m, cm): ")
cantidad=int(input(f"Ingrese la cantidad de {unidades}: "))
operacion=cantidad*unidades_metros[unidades]
print(f"{cantidad} a metros es: {operacion}")

print("Punto 11")
print("Lista de productos mas IVA")
precios_=[float(input("Ingrese el precio uno: ")),float(input("Ingrese el precio dos: ")),float(input("Ingrese el precio tres: ")),float(input("Ingrese el precio cuatro: ")),float(input("Ingrese el precio cinco: "))]
precio_uno_iva=precios_[0]+((precios_[0]*19)/100)
precio_dos_iva=precios_[1]+((precios_[1]*19)/100)
precio_tres_iva=precios_[2]+((precios_[2]*19)/100)
precio_cuatro_iva=precios_[3]+((precios_[3]*19)/100)
precio_cinco_iva=precios_[4]+((precios_[4]*19)/100)
precios_IVA=[precio_uno_iva,precio_dos_iva,precio_tres_iva,precio_cuatro_iva,precio_cinco_iva]
print(f"Los precios originales son: {precios_}\nLos precios con el 19% de IVA son: {precios_IVA}")

print("Punto 12")
print("Tupla de operaciones matematicas")
numero_uno=int(input("Ingrese el primer numero: "))
numero_dos=int(input("Ingrese el segundo numero: "))
suma=numero_uno+numero_dos
resta=numero_uno-numero_dos
multiplicacion=numero_uno*numero_dos
division=round(numero_uno/numero_dos,2)
operaciones=(suma,resta,multiplicacion,division)
print(f"Los numeros ingresados son: {numero_uno} y {numero_dos}\nEl resultado de la suma, resta, multiplicacion y division de los numeros son: {operaciones}")

print("Punto 13")
print("Diccionario de estudiantes")
estudiantes={"marcelo":3.6,"Agustin":4,"Frederic":5}
promedio=round(sum(list(estudiantes.values()))/len(estudiantes),1)
print(f"Los estudiantes y sos notas son: {estudiantes}\nEl promedio general de las notas es: {promedio}")

print("Punto 14")
print("Lista de salarios")
salario_uno=float(input("Ingrese el salario uno: "))
salario_dos=float(input("Ingrese el salario dos: "))
salario_tres=float(input("Ingrese el salario tres: "))
salario_cuatro=float(input("Ingrese el salario cuatro: "))
salario_cinco=float(input("Ingrese el salario cinco: "))
salarios=[salario_uno,salario_dos,salario_tres,salario_cuatro,salario_cinco]
salario_uno_aumento=salarios[0]+((salarios[0]*10)/100)
salario_dos_aumento=salarios[1]+((salarios[1]*10)/100)
salario_tres_aumento=salarios[2]+((salarios[2]*10)/100)
salario_cuatro_aumento=salarios[3]+((salarios[3]*10)/100)
salario_cinco_aumento=salarios[4]+((salarios[4]*10)/100)
salarios_aumento=[salario_uno_aumento,salario_dos_aumento,salario_tres_aumento,salario_cuatro_aumento,salario_cinco_aumento]
print(f"Los salarios originales son: {salarios}\n Los salarios con el aumento del 10% son: {salarios_aumento}")

print("Punto 15")
print("Diccionario de impuestos")
productos_={"carbon":2000,"anillos":15600,"sillas":5000}
print(f"Los productos y sus precios son: {productos_}")
porcetaje_impuesto=int(input("Ingrece el porcentaje de impuesto para los productos: "))
productos_["carbon"]=productos_["carbon"]+((productos_["carbon"]*porcetaje_impuesto)/100)
productos_["anillos"]=productos_["anillos"]+((productos_["anillos"]*porcetaje_impuesto)/100)
productos_["sillas"]=productos_["sillas"]+((productos_["sillas"]*porcetaje_impuesto)/100)
print(f"Los productos y su precio con el impuesto son: {productos_}")

print("Punto 16")
print("Analisis de lista de edades")
edades_=[int(input("Ingrese la edad uno: ")),int(input("Ingrese la edad dos: ")),int(input("Ingrese la edad tres: ")),int(input("Ingrese la edad cuatro: ")),int(input("Ingrese la edad cinco: "))]
mayores_18=edades[0]>18+edades[1]>18+edades[2]>18+edades[3]>18+edades[4]>18
print(f"Hay {mayores_18} mayores de edad y {len(edades_)-mayores_18} menores  de edad")

print("Punto 17")
print("Tupla de conversiones de moneda")
dolares=float(input("Ingrese la cantidad en dolares para convertir a euros, pesos y yenes: "))
euros=dolares*0.85020
pesos=dolares*4014.96
yenes=dolares*143.68
dolar_monedas=(euros,pesos,yenes)
print(f"{dolares} a euros, pesos y yenes es: {dolar_monedas}")

print("Punto 18")
print("Diccionario de ventas")
productos_ventas={}
productos_ventas[input("Ingrese el nombre del producto uno: ")]=int(input("Ingrese la cantidad comprada del producto uno: "))
productos_ventas[input("Ingrese el nombre del producto dos: ")]=int(input("Ingrese la cantidad comprada del producto dos: "))
productos_ventas[input("Ingrese el nombre del producto tres: ")]=int(input("Ingrese la cantidad comprada del producto tres: "))
total_unidades=sum(list(productos_ventas.values()))
print(f"Los productos y su cantidad ingresados son: {productos_ventas}")
print(f"El total de las unidades vendidas es: {total_unidades}")

print("Punto 19")
print("Lista de temperaturas extremas")
temperaturas=[34,67,12,49,23,10,6,1,100,99]
print(f"Las temperaturas ingresadas son: {temperaturas}")
mayor_verdadero=[temperaturas[0]>30,temperaturas[1]>30,temperaturas[2]>30,temperaturas[3]>30,temperaturas[4]>30,temperaturas[5]>30,temperaturas[6]>30,temperaturas[7]>30,temperaturas[8]>30,temperaturas[9]>30]
menor_verdadero=[temperaturas[0]<10,temperaturas[1]<10,temperaturas[2]<10,temperaturas[3]<10,temperaturas[4]<10,temperaturas[5]<10,temperaturas[6]<10,temperaturas[7]<10,temperaturas[8]<10,temperaturas[9]<10]
mayor30=[temperaturas[0]*mayor_verdadero[0],temperaturas[1]*mayor_verdadero[1],temperaturas[2]*mayor_verdadero[2],temperaturas[3]*mayor_verdadero[3],temperaturas[4]*mayor_verdadero[4],temperaturas[5]*mayor_verdadero[5],temperaturas[6]*mayor_verdadero[6],temperaturas[7]*mayor_verdadero[7],temperaturas[8]*mayor_verdadero[8],temperaturas[9]*mayor_verdadero[9],0]
menor10=[temperaturas[0]*menor_verdadero[0],temperaturas[1]*menor_verdadero[1],temperaturas[2]*menor_verdadero[2],temperaturas[3]*menor_verdadero[3],temperaturas[4]*menor_verdadero[4],temperaturas[5]*menor_verdadero[5],temperaturas[6]*menor_verdadero[6],temperaturas[7]*menor_verdadero[7],temperaturas[8]*menor_verdadero[8],temperaturas[9]*menor_verdadero[9],0]
mayor30=set(mayor30)
mayor30.remove(0)
mayor30=list(mayor30)
menor10=set(menor10)
menor10.remove(0)
menor10=list(menor10)
print(f"Las temperaturas mayores a 30 son: {mayor30}")
print(f"Las temperaturas menores a 10 grados son: {menor10}")

print("Punto 20")
print("Actualizar precios con metodos de listas")
precios_actualizar=[1000,2000,3000,4000,5000]
print(f"Los precios disponibles son: {precios_actualizar}")
eliminar=int(input("Ingrese el precio a eliminar: "))
precios_actualizar.remove(eliminar)
agregar=int(input("Ingrese el precio para agregar: "))
precios_actualizar.append(agregar)
print(f"Los precios de menor a mayor son: {sorted(precios_actualizar)}")


