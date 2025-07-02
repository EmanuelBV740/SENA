persona = {
    "nombre":"juan",
    "edad":"30",
    "L.naciomiento": "palmira",
    "celular" : "312894536",
    "profe" : "programador",
    "celuda": 13243549878,

}
print (f"{persona}")

auto = {
    "marca": "frod",
    "modelo": "mustang",
    "año" : 2012,
    "placa": "dex309",
    "valor": "$400000",
    "vendido": False,
    "Color": "azul",
    "abulladuras": True,
    "rayones": True,
    "estrellenes": False,

}
print (f"vieja: {auto}")

print (auto ["modelo"])

auto ["vendido"] = True

auto ["Color"] = "rojo" 

del auto ["placa"]
auto.pop ("marca")
print (f"nueva: {auto}")

del auto ["abulladuras"]
auto.pop ("rayones")
print (f"moderna: {auto}")

