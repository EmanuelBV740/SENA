# #1
# total = 0 
# num = int(input("dame un numero entero: "))
# while num != 0:
#     total += num
#     num = int(input("dame un numero entero: "))
# print (f"suma tota es {total}")

# #2
# contraseña = ""
# while contraseña != "python123":
#     contraseña = input("dame la contraseña: ")
# print (f"correcto")

# #3
# lista = []
# producto = ""
# while producto != "fin":
#     producto = input ("dame un producto o sal del sistema (fin): ")
#     if producto != "fin":
#         lista.append(producto)
# print (lista)

# #4
# cont = 1
# pares = 0
# impares = 0
# while cont <= 10:
#     numero = int (input(f"dame el numero {cont}: "))
#     if numero %2 == 0:
#         pares += 1
#     else:
#         impares += 1
#     cont += 1
# print (f"los pares son {pares}")
# print (f"los impares son {impares}")

# #5
# notas = []
# n_notas = 1
# print (f"ingresa 5 notas ")
# while n_notas <= 5:
#     nota = float(input(f"dame la nota {n_notas}: "))
#     n_notas += 1
#     notas.append (nota)
#     salir = input ("¿salir? (si/no): ")
#     if salir == "si":
#         print("saliste")
#         break
#     suma = sum (notas)
#     divir = suma / 5
# print (f"las notas son {notas} y el promedio es {divir}")

# #6
# nmu_1 = int(input("ingrasa la tabla de multiplicar deseada: "))
# i=1
# print (f"\ninicia el contador en 1 {nmu_1}: ")
# while i<= 10:
#     print (f"{nmu_1}*{i}={nmu_1*i}")
#     i+=1

# #7
# numero_secreto : 17
# intento = 1
# num = ""
# while num != 17:
#     num = int(input(f"dame un numero (intento {intento})")) 
#     intento += 1
# print (f"lo lograste (intentos {intento})")

# #8
# frutas = ("manzana","pera","limon")
# while True:
#     fruta = input("dame una fruta: ")
#     print ("no lo lograste sigue intentando")
#     if fruta in frutas:
#         print (f"lo lograste tu tupla era {frutas}")
#         break

#9
palabras = {
    "carro":"car",
    "dia": "day",
    "ciudad": "city",
    "grande": "gig",
    "llave": "key"
}
num = ""
while True:
    num = input ("dame una palabra en español: ")
    if num in palabras:
        print (f"la palabra si esta y es: {palabras [num]}")
    else:
        print (f"la palabra {num} no esta ")

#10























