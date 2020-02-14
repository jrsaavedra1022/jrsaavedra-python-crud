print("Operaciones con las listas ...\n")
a = [1, 2]
b = [2, 3]
c = a + b
print("Suma de listas: {}".format(c))
a = [1, 2]
b = a*2
print("multiplicacion de listas: {}".format(b))

print("\n Lista de range ...")
# start, end. jumps
a = list(range(0, 50, 2))
b = list(range(0, 10))
c = a + b
print(c)
print(b*3)

print("Append in lists")
fruits = list()
fruits.append("apple")
fruits.append("orange")
fruits.append("banana")
print("list's fruits: {}".format(fruits))
fruits.pop()
print(fruits)
del fruits[0]
print(fruits)

# listas aleatorios
import random

list_random = []
for i in range(10):
	list_random.append(random.randint(0, 15))

print("Lista de numero aleatorios: {}".format(list_random))
ordered_numbers = sorted(list_random)
print("Ordenar lista de número aleatorios: {}".format(ordered_numbers))