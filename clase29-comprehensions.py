lista_de_numeros = list(range(100))
print(lista_de_numeros)
# numero pares
pares = [numero for numero in lista_de_numeros if numero % 2 == 0]
print("\nPares: {}".format(pares))
# genrando diccionarios
student_uid = [1, 2, 3]
students = ['Juan', 'Jose', 'Larsen']
students_with_uid = {uid: student for uid, student in zip(student_uid, students)}
print("\nDiciconario: {}".format(students_with_uid))

import random
random_numbers = []
for i in range(10):
	random_numbers.append(random.randint(1, 3))

print("\nNumero aleatorios: {}".format(random_numbers))

# numeros no repetidos
non_repeated = set([number for number in random_numbers])
print("\nNúmeros no repetidos: {}".format(non_repeated))