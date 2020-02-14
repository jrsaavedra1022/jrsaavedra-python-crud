print("Manejo de diccionarios ...")

rae = {}
rae['pizza'] = 'La comida más deliciosa del mundo'
rae['pasta'] = 'La comida más sabrosa de Italia'

print(rae)
print(rae['pizza'])

a = rae.get("helado", None)
print(a)

a = rae.get("pizza", None)
print(a)

llaves = rae.keys()
valores = rae.values()
tuplas_valores = rae.items()

print("\n")
print("Llaves del diccionario: {}  \n".format(llaves))
print("Valores del diccionario: {}  \n".format(valores))
print("tuplas de valores del diccionario: {}  \n".format(tuplas_valores))

# iterar diccionarios

print("\n GET KEYS ....")
for key in rae.keys():
	print("key: {}".format(key))


print("\n GET VALUES ....")
for value in rae.values():
	print("value: {}".format(value))


print("\n GET ITEMS ....")
for key, value in rae.items():
	print("key: {}, value: {}".format(key, value))

print("End iterator cicles")


print("Know methods in function: ")
print(dir(rae))