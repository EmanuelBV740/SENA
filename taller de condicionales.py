# #primera
# edad = int(input("dame tu edad: "))
# if edad < 18:
#     print (f"tiees {edad}, eres menor de edad")
# elif edad >= 18:
#     print (f"tienes {edad}, eres un mayor de edad")
# elif edad >= 65:
#     print (f"tienes {edad}, eres un adulto mayor")
# #segunda
# altura = (float(input("dame tu estaruca en metros: ")))
# if altura < 1.5: 
#     print (f"estatura baja") 
# elif altura > 1.5 < 1.8:
#     print (f"estatura media")
# elif altura > 1.8:
#     print (f"estatura alta")
# #tercera
# num1 = (float(input("dame un numero para ver su multiplo: ")))
# if num1 % 2 == 0 and num1 % 3 == 0:
#      print (f"{num1} es multiplo de los dos")
# elif num1 % 2 == 0:
#      print (f"{num1} multiplo de 2")
# elif num1 % 3 == 0:
#      print (f"{num1} multiplo de 3")
# else:
#     print (f"el numero {num1} no es multiplo de ninguno")
# #cuarta
# num2 = input ("dame un numero decimal: ")
# decimales = num2.split (".")
# if len (decimales) == 2:
#      decimales2 = decimales [1]
#      cantidad =len(decimales2)
#      if cantidad == 1:
#           print(f"{num2} tiene un decmal") 
#      elif cantidad == 2:
#           print (f"{num2} tiene dos decimales")
#      else:
#           print (f"{num2} tiene mas de dos decimales") 
# else:
#      print (f"{num2} no tiene decimales")
# #quinta
# tupla = ("colombia","peru","argentina","mexico")
# pais = (input("dame tu pais: "))
# if pais in tupla:
#      print (f"{pais} esta en la tupla")
# elif pais in tupla:
#      print (f"{pais} no esta en la tupla")
# sexta
# tipo_de_sangre ={
#      "A": ["eres compatible a sangre tipo A o tipo O."], 
#      "B": ["eres compatible a sangre tipo B o tipo O."], 
#      "AB": ["eres compatible a sangre de cualquier grupo (A, B, AB o O)."], 
#      "O" : ["eres compatible a sangre únicamente de tipo O."]
#      }
# sangre = input("ingrasa tu tipo de sangre (A,B,AB,O): ")
# if sangre == "A":
#      print (f"puedes donar a: A y O")
# elif sangre == "B":
#      print (f"eres compatible a: B y O")
# elif sangre == "AB":
#      print (f"eres compatible a: A, B, AB y O")
# elif sangre == "O":
#      print (f"eres compatible a: O")
# else:
#      print (f"no hay bse de datos")
# septima
# temperatura = int(input("dame una temperatura en C°: "))
# if temperatura < 10:
#      print (f"hace frio")
# elif temperatura >= 10 and temperatura <=25:
#      print (f"esta templado")
# else:
#      print (F"hace calor")
# octava
# opera = input("dame una operacion matematica (suma, resta, multiplicacion): ")
# numero1 = int(input("primer numero: "))
# numero2 = int(input("segundo numero: "))
# if opera == "multiplicacion":
#      m= numero1 * numero2
#      print (f"{m}")
# elif opera == "suma":
#      s= numero1 + numero2
#      print (f"{s}")
# elif opera == "resta":
#      r= numero1 - numero2
#      print (f"{r}")
# else:
#      print(f"operacion invalida")
# #novena
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
     























