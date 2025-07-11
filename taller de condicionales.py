#primera
edad = int(input("dame tu edad: "))
if edad < 18:
    print (f"tiees {edad}, eres menor de edad")
elif edad >= 18:
    print (f"tienes {edad}, eres un mayor de edad")
elif edad >= 65:
    print (f"tienes {edad}, eres un adulto mayor")
#segunda
altura = (float(input("dame tu estatura en metros: ")))
if altura < 1.5: 
    print (f"estatura baja") 
elif altura > 1.5 < 1.8:
    print (f"estatura media")
elif altura > 1.8:
    print (f"estatura alta")
#tercera
num1 = (float(input("dame un numero para ver su multiplo: ")))
if num1 % 2 == 0 and num1 % 3 == 0:
     print (f"{num1} es multiplo de los dos")
elif num1 % 2 == 0:
     print (f"{num1} multiplo de 2")
elif num1 % 3 == 0:
     print (f"{num1} multiplo de 3")
else:
    print (f"el numero {num1} no es multiplo de ninguno")
#cuarta
num2 = input ("dame un numero decimal: ")
decimales = num2.split (".")
if len (decimales) == 2:
     decimales2 = decimales [1]
     cantidad =len(decimales2)
     if cantidad == 1:
          print(f"{num2} tiene un decmal") 
     elif cantidad == 2:
          print (f"{num2} tiene dos decimales")
     else:
          print (f"{num2} tiene mas de dos decimales") 
else:
     print (f"{num2} no tiene decimales")
#quinta
tupla = ("colombia","peru","argentina","mexico")
pais = (input("dame tu pais: "))
if pais in tupla:
     print (f"{pais} esta en la tupla")
elif pais in tupla:
     print (f"{pais} no esta en la tupla")
#sexta
tipo_de_sangre ={
     "A": ["eres compatible a sangre tipo A o tipo O."], 
     "B": ["eres compatible a sangre tipo B o tipo O."], 
     "AB": ["eres compatible a sangre de cualquier grupo (A, B, AB o O)."], 
     "O" : ["eres compatible a sangre únicamente de tipo O."]
     }
sangre = input("ingrasa tu tipo de sangre (A,B,AB,O): ")
if sangre == "A":
     print (f"puedes donar a: A y O")
elif sangre == "B":
     print (f"eres compatible a: B y O")
elif sangre == "AB":
     print (f"eres compatible a: A, B, AB y O")
elif sangre == "O":
     print (f"eres compatible a: O")
else:
     print (f"no hay bse de datos")
#septima
temperatura = int(input("dame una temperatura en C°: "))
if temperatura < 10:
     print (f"hace frio")
elif temperatura >= 10 and temperatura <=25:
     print (f"esta templado")
else:
     print (F"hace calor")
#octava
opera = input("dame una operacion matematica (suma, resta, multiplicacion): ")
numero1 = int(input("primer numero: "))
numero2 = int(input("segundo numero: "))
if opera == "multiplicacion":
     m= numero1 * numero2
     print (f"{m}")
elif opera == "suma":
     s= numero1 + numero2
     print (f"{s}")
elif opera == "resta":
     r= numero1 - numero2
     print (f"{r}")
else:
     print(f"operacion invalida")
#novena
meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}
calendario = int(input("dame un numero del 1 al 12: "))
if 1<=calendario<=12:
     print (f"tu mes es {meses[calendario]}")
else:
     print ("numero no valido")
#decima
numero = input("10. Ingresa un número de 4 dígitos: ")
if numero.startswith('1'):
    print("Empieza con 1")
elif numero.startswith('2'):
    print("Empieza con 2")
else:
    print("Empieza con otro número")

#onceava
palabra = input("11. Ingresa una palabra: ")
primera = palabra[0]
if primera.isdigit():
    print("La primera letra es un número")
elif primera.lower() in "aeiou":
    print("La primera letra es una vocal")
else:
    print("La primera letra es una consonante")

#doceava
frutas = {"manzana": 3000, "pera": 2500, "piña": 4000}
fruta = input("12. Ingresa una fruta: ")
if fruta in frutas:
    print(f"El precio de la {fruta} es ${frutas[fruta]}")
else:
    print("Fruta no disponible")

#treceava
nota = float(input("13. Ingresa tu calificación (0 a 5): "))
if nota < 3:
    print("Reprobado")
elif nota <= 4:
    print("Aprobado")
else:
    print("Excelente")

#cartoceava
num = int(input("14. Ingresa un número: "))
if num % 4 == 0:
    print("Es divisible entre 4")
elif num % 6 == 0:
    print("Es divisible entre 6")
else:
    print("No es divisible ni por 4 ni por 6")

#quinceava
usuarios = {"admin": "1234", "juan": "abcd", "ana": "pass"}
user = input("15. Usuario: ")
clave = input("Clave: ")
if user in usuarios and usuarios[user] == clave:
    print("Autenticación exitosa")
else:
    print("Usuario o clave incorrecta")

#diesisiesava
edad = int(input("16. Ingresa tu edad: "))
if 0 <= edad <= 12:
    print("Niño")
elif edad <= 17:
    print("Adolescente")
elif edad <= 64:
    print("Adulto")
else:
    print("Mayor")

#diesisieteava
capitales = ("bogotá", "medellín", "cali", "cartagena")
ciudad = input("17. Ingresa una ciudad: ")
if ciudad in capitales:
    print("Es una ciudad capital")
else:
    print("Ciudad secundaria")

#diesiochoava
compra = float(input("18. Valor de la compra: "))
if compra > 200000:
    total = compra * 0.85
    print(f"Aplica 15% de descuento. Total a pagar: ${total:.2f}")
elif compra >= 100000:
    total = compra * 0.90
    print(f"Aplica 10% de descuento. Total a pagar: ${total:.2f}")
else:
    print(f"No aplica descuento. Total a pagar: ${compra:.2f}")

#diesinueveava
nombre = input("19. Nombre del trabajador: ")
horas = int(input("Horas trabajadas: "))
tarifa = 10000
salario = horas * tarifa
if horas > 40:
    bono = salario * 0.20
    salario += bono
    print(f"{nombre} trabajó más de 40 horas. Salario con bono: ${salario}")
else:
    print(f"{nombre} trabajó {horas} horas. Salario: ${salario}")

#veinteava
puntaje = int(input("20. Ingresa tu puntaje (0 a 100): "))
if puntaje < 50:
    print("Insuficiente")
elif puntaje < 80:
    print("Aceptable")
else:
    print("Sobresaliente")
























