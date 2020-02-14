# tuplas
a = (1,2,3)
print("Tupla: {}".format(a))
print("Index tupla: {}".format(a[0]))

# No se puede modificar la tupla
# a[0] = 10

# methods from tuple
a = (1,2,3,1,4,5,6,5,7)
methods_tuple = dir(a)
print("Tupla con elementos repetidos: {}".format(a))
print("Elemento en la tupla cantidad de veces: {}".format(a.count(1)))
print("Indice del elemento por primera vez: {}".format(a.index(1)))
print("")
print("*"*10)

# conjuntos
a = set([1,2,3])
b = set([3,4,5])

print("Conjunto: {}".format(a))
a.add(3)
print("Los conjuntos NO pueden tener duplicados: {}".format(a))
a.add(20)
print("Agregar valores a los conjuntos: {}".format(a))
print("-"*10)
print("Interseccion de los conjuntos {}".format(a.intersection(b)))
print("Union de los conjuntos {}".format(a.union(b)))
print("Diferencia de los conjuntos {}".format(a.difference(b)))
print("Diferencia de los conjuntos {}".format(b.difference(a)))
print("\n Elimninar elementos de nuestro set")
a.remove(1)
print("Elemento 1 eleminado del conjunto: {}".format(a))