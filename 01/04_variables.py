# Variables

# Asignar una variable

my_name = "John"

print(my_name)

age = 30
print(age)

age = 31  # Reasignar una variable
print(age)

# Tipado dinámico
# No es necesario declarar el tipo de dato al asignar una variable

name = "Alice" # Variable de tipo str, no es necesario especificar el tipo
print(type(name))

name = 25  # Ahora es una variable de tipo int
print(type(name))

# Tipado fuerte
# No se puede realizar operaciones entre tipos diferentes sin convertirlos
# print(name + 5)  
# # Esto generaría un error porque name es un int y 5 es un int, pero no se pueden sumar directamente