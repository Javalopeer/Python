'''
Sentencias condicionales
if, elif, else
'''

import os 
os.system("cls")

print("\n---Sentencia simple condicional:")
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
edad = 15
if edad >= 18:
    print("Eres mayor de edad")


print("\n---Sentencia condicional con else:")
edad = 15
if edad >= 18:
    print(f"Eres mayor de edad")
else:
    print(f"Eres menor de edad")


print("\n---Sentencia condicional con elif:")
nota = 2
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")


print("\n---Condiciones multiples:")
edad = 16
tiene_carnet = False

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir")


print("\n---Condiciones con or:")
if edad >= 18 or tiene_carnet:
    print("Puedes conducir")
else:
    print("Paga al policia y te deja conducir")


print("\n---Condiciones con not:")
es_fin_de_semana = False
if not es_fin_de_semana:
    print("A trabajar")
else:
    print("A descansar")