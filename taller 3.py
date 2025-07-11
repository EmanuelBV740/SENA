# # #primera
# # num1 = (float(input("dame un numero negativo o positiva: ")))
# # if num1 > 0:
# #     print (f"{num1} es positivo")
# # elif num1 < 0:
# #     print (f"{num1} es negativo")
# # else: 
# #     print (f"{num1} no esta en la programacion")
# # #segunda
# # num2 = (float(input("dame un numero: ")))
# # num3 = (float(input("dame un numero: ")))
# # if num2 > num3:
# #     print (f"{num2} es mayor que {num3}")
# # elif num3 > num2:
# #     print (f"{num3} es mayor que {num2}")
# # else:
# #     print (f"son iguales")
# #tercera
# num4 = (float(input("dame un numero para ver si es par o inpar: ")))
# if num4 % 2 == 0:
#     print (f"{num4} es par")
# else:
#     print (f"{num4} es inpar")
# #cuarto
# num5 = (float(input("dame un numero para ver si esta dento de 10 y 20: ")))
# if 10 <= num5 <= 20:
#     print (f"{num5} si esta")
# else:
#     print (f"{num5} no esta ")
# #quinta
# num6=(float(input("dame un numero: ")))
# num7=(float(input("dame un numero: ")))
# num8=(float(input("dame un numero: ")))##holaaaaaaaaaaa
# if num6 > num7 and num6 > num8:
#     print (f"{num6}es el mayor")
# elif num7 > num6 and num7 > num7:
#     print (f"{num7} es el mayor")
# else:
#     print (f"{num8} es el mayor")
#sexta
total_dinero = (float(input("ingrasa total de la compra: ")))
if total_dinero > 100:
    total_dinero *= 0.9
    print (f"descuento del total: {total_dinero}")
else:
    print (f"el descuento no aplica")
#septima
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Puede votar.")
else:
    print("No puede votar.")
#octavo
precio = float(input("Ingrese el precio: "))
tipo = input("Ingrese tipo de cliente (VIP o normal): ")

if tipo == "vip":
    precio *= 0.8

print(f"Precio final: ${precio:.2f}")
#noveno
num = int(input("Ingrese un número: "))
if num % 3 == 0 and num % 5 == 0:
    print("Es múltiplo de 3 y 5.")
else:
    print("No es múltiplo de 3 y 5.")
#decimo
num = int(input("Ingrese el número a verificar: "))
div1 = int(input("Ingrese el primer divisor: "))
div2 = int(input("Ingrese el segundo divisor: "))

if num % div1 == 0 and num % div2 == 0:
    print(f"{num} es divisible entre {div1} y {div2}.")
else:
    print(f"{num} no es divisible entre ambos.")
















