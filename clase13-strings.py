country = 'colombia'

# se comienza a contar desde cero
print("posicion 0: {}".format(country[0]))
print("posicion -1: {}".format(country[-1]))

# se comienza a contar desde 1
print("cantidad de caracteres: {}".format(len(country)))

second_letter = country[1]
print(second_letter)
# ver la direccion en memoria de nuestra computadora
print(id(second_letter))


other_letter = "o"
print(other_letter)
print(id(other_letter))