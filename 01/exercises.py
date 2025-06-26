'''
print("\nEjercicio 1: Imprimir mensajes: ")
print("Escribe un programa que imprima tu nombre y tu ciudad en lineas separadas.")

nombre, ciudad = input("Ingresa tu nombre y ciudad: ").split()
print(f"Te llamas {nombre} y vives en {ciudad}.")
print(f"{nombre} {ciudad}.")

'''

'''

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable")

a = 15
b = 3.14159
c = "Hola Mundo"
d = True
e = None

print("a:" , type(a))
print("b:" , type(b))
print("c:" , type(c))
print("d:" , type(d))
print("e:" , type(e))

'''

'''
print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. Que ocurre?")


cadena = "12345"
numero_entero = int(cadena) 
numero_float = float(cadena)

print("Numero entero: ", numero_entero)
print("Numero como float: ", numero_float)

float = 3.99
entero_convertido = int(float)

print("Numero convertido: ", entero_convertido)

'''
'''

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación")

nombre, edad = input("Cual es tu nombre y edad? ").split(" ")
altura = input("Cual es tu altura? ")
print(f"Hola {nombre}, tienes {edad} años y tu altura es de {altura} metros.")

'''

print("\nEjercicio 5: Numeros")
resultado = int(round(3.14159)/2)

print("Valor de PI (aproximado):", 3.1416)
print("PI redondeado:", round(3.1416))
print("División entera de PI redondeado entre 2:", resultado)