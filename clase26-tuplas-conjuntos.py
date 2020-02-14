print("Manejo de tuplas ...")
# tuplas son iguales a las lista pero son inmutables
a = (1,2)
print("Tuple: {}".format(a))
# conjuntos=> los set si son mutables => no existe valres repetidos

b = set([1,2,3])
c = set([2,4,5])
print("Union de conjuntos: {}".format(b.union(c)))
print("Diferencia de conjuntos: {}".format(b.difference(c)))
