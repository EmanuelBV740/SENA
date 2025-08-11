vocal= input ("dame una vocal en minuscula: ")
if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal ==  "u":
    mayus=vocal.upper ()
    print (F"la vocal en mayuscula es: {mayus}")
else:
    print (f"no es una vocal ")

"""1"""
num = float (input ("dame un numero: "))
if num < 0:
    print (f"es negativo")
elif num > 0:
    print (f"es numero es +")
else:
    print (f"es cero")
"""2"""
num1 = float (input ("dame un numero: "))
num2 = float (input ("dame un numero: "))
if num1 < num2:
    print (f"{num1} es menosr que {num2}")
elif num1 > num2:
    print (f"{num1} es mayar que {num2}")
else:
    print (f"es igual")
"""3"""
valor = float (input ("dame un numero: "))
if valor % 2 :
    print (f"es impar")
elif valor % 3:
    print (f"es par")
else:
    print (f"no es un numero")
"""4"""
numero = float (input ("dame un numero: "))
if numero < 10 and numero >20:
    print (f"no es de la familia")
elif numero > 10 and numero <20:
    print (f"es de la familia")
else:
    print (f"no es un numero conocido por mi ")
"""5"""
valor1 = float (input ("dame un numero: "))
valor2 = float (input ("dame un numero: "))
valor3 = float (input ("dame un numero: "))
if valor1 >= valor2 and valor1 >= valor3:
    print (f"el numero mayor es {valor1}")
elif valor2 >= valor3:
    print (f"el mayor es {valor2}")
else:
    print (f"el mayor es {valor3}")
"""6"""
valor_total = float (input ("dame el valor total: "))
if valor_total > 100:
    descuento = valor_total * 0.10
    precio_final = valor_total - descuento
else:
    precio_final = valor_total
print (f"el descuento final es de {precio_final}")
"""7"""
edad = int (input ("dame tu edad actual: "))
if edad <= 17:
    print(f"no puedes votar eres menor de edad (tu edad es {edad})")
elif edad >= 18:
    print (f"si puedes votar eres mayor de edad (tienes {edad})")
else:
    print (f"no exixte esa edad")
"""8"""
precio = int (input ("dame un precio: "))
cliente = input ("que menbresia eres? (VIP/NORMAL): ").lower()
if cliente == "vip":
    descuento= precio * 0.20
    print (F"tu descuento es de {descuento}")
elif cliente == "normal":
    print (f"no tienes descuento, precio final {precio}")
"""9"""
num = int(input("ingresa un número: "))
if num % 3 == 0 and num % 5 == 0:
     print("es múltiplo de 3 y 5")
else:
    print("no es muliplo de 3 y 5")
"""10"""
n = 20
d1 = 2
d2 = 5
if n % d1 == 0 and n % d2 == 0:
    print("Es divisible entre ambos")
else:
    print("No es divisible entre ambos")
"""11"""
lista = [3, 7, 15, 8, 2]
if lista[2] >= 10:
    print (f"Mayor a 10")
else:
    print ("Menor o igual a 10")
"""12"""
lista = [3, 5, 7, 9]
if 7 in lista:
    print("Está en la lista") 

else: 
    print ("No está en la lista")
"""13"""
lista = [4, 6, 2, 8]
suma = lista[0] + lista[1]
if suma > 10:
    print("Suma alta")
else:
    print("Suma baja")

"""14"""
nombres = ["Ana", "Luis", "Pedro", "Marta"]
ultimo = input ("dame el ultimo nombre de la tabla: ")
if ultimo == "Marta":
    print("Nombre correcto") 
else:
    print ("Nombre diferente")
print (nombres)

if nombres [-1] == "marta":
    print ("nombre correcto")









"""15"""
colores = ["rojo", "azul", "verde"]
if colores[1] == "azul":
    colores[1] = "amarillo"
print("Colores:", colores)

"""16"""
tupla = (5, 8, 12, 20)
if tupla[0] < tupla[-1]:
    print("Orden ascendente") 
else:
    print ("Orden descendente")

"""17"""
tupla = (25, 32, 28)
if tupla[1] > 30:
    print("Edad mayor a 30") 
else:
    print ("Edad menor o igual a 30")
"""18"""
tupla = (1, 2, 3)
lista = list(tupla)
if lista[1] == 2:
    lista[1] = 10
tupla = tuple(lista)
print("Tupla modificada:", tupla)

"""19"""
tupla = (4, 9)
if tupla[1] > 5:
    print("Coordenada alta")
else:
    print ("Coordenada baja")

"""20"""
t1 = (3, 4)
t2 = (3, 5)
if t1 == t2:
    print("Tuplas iguales")
else:
    print("Tuplas diferentes")

"""21"""
persona1 = {"nombre": "Juan",
           "edad": int(input("dame tu edad")),
           }
print (persona1)
if persona1["edad"] >= 18:
    print("Adulto")
else:
    print ("Menor de edad")
"""22"""
persona2 = {"nombre": "Lucía", 
           "edad": int(input("dame tu edad")),
           }
print (persona2)
if persona2["edad"] > 18:
    persona2["edad"] = 21
print(persona2)

"""23"""
persona3 = {"nombre": "Carlos"}
print (persona3)
if "ciudad" not in persona3:
    persona3["ciudad"] = "Bogotá"
print(persona3)

"""24"""
producto = {"producto": "pan",
            "precio": 1200,
            }
if "precio" in producto:
    print(f"producto precios: {producto ['precio']}")
else:
    print("No hay precio")
"""25"""
productos = {"pan": 1200,
            "leche": 2000,
            }
if "pan" in productos:
    print (f"producto: {productos["pan"]}")
else:
    print ("Producto no disponible")






