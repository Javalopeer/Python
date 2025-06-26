#Entrada de usuarios
#input_usuario = input("Ingrese un valor: ")
# print(input_usuario)


print("Como te llamas?")
nombre = input()
print(f"Hola,  {nombre} !")

age = input("Cuantos años tienes? ")
print(type(age))
print(f"Detro de 20 años tendras {int(age) + 20} años.")

print("Obtener multiples valores a la vez")
country, city = input("En que pais y ciudad vives? ").split()
print(f"Vives en {city}, {country}.")
