# operaciones con strigs
platzi = 'platzi'
print(platzi)

print("Mayusculas: {}".format(platzi.upper()))
print("Minusculas: {}".format(platzi.lower()))
print("Encontrar posicion: {}".format(platzi.find('la')))
print("word start with: {}".format(platzi.startswith('p')))
print("word end with: {}".format(platzi.endswith('i')))

# funcion para saber que puedo hacer con esa variable o elemento
print("I do with a element")
print(dir(platzi))


# Texto de ayuda para un function
def my_function():
	""" Estos es el texto de ayuda para esta funcion """
	pass

help(my_function)