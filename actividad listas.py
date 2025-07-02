lista1 = [1,2,3,4,5]
lista2 = ["a","b","c"]

"""primer punto"""
lista1.append(100)
lista1.append("hola mundo")
"""segundo punto"""
lista2.append("hola")
lista2.append("adios")
lista2.append(300)
"""punto 3"""
lista3 = lista1.copy()
lista3.pop()
"""punto 4"""
lista4=lista2[1:-1]
"""punto 5"""
lista5 = lista3 + lista4
"""prints"""
print (f"lista 1 {lista1}")
print (f"lista 2 {lista2}")
print (f"lista 3 {lista3}")
print (f"lista 4 {lista4}")
print (f"lista 5 {lista5}")