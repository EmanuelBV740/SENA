# Ejercicio 1: Crear una tupla con los números del 1 al 5
tupla1 = (1, 2, 3, 4, 5)
print(f"Tupla: {tupla1}")

# Ejercicio 2: Acceder a un elemento - Mostrar el segundo valor
print(f"Segundo valor: {tupla1[1]}")

# Ejercicio 3: Obtener la longitud
print(f"Longitud de la tupla: {len(tupla1)}")

# Ejercicio 4: Usar index() - Posición del número 4
print(f"Posición del número 4: {tupla1.index(4)}")

# Ejercicio 5: Usar count() - Cuántas veces aparece el número 2
print(f"Cantidad de veces que aparece el 2: {tupla1.count(2)}")

# Ejercicio 6: Tupla con tipos mezclados
tupla_mixta = ("texto", 10, 3.14)
print(f"Tupla con tipos mezclados: {tupla_mixta}")

# Ejercicio 7: Tuplas anidadas - Acceder al primer valor de la tupla interna
tupla_anidada = ((100, 200), "otro valor", 50)
print(f"Primer valor de la tupla interna: {tupla_anidada[0][0]}")
