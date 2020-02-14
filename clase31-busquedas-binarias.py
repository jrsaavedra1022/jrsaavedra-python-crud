# busquedas binarias de elmentos en pýthon
# para consultas más eficientes en python
import random


# funcion de recursión
def binary_search(data, target, low_index, high_index):
	if low_index > high_index:
		return False

	mid_index = (low_index + high_index) // 2
	print("Indice medio: {}".format(mid_index))

	if target == data[mid_index]:
			return True
	elif target < data[mid_index]:
		return binary_search(data, target, low_index, mid_index - 1)
	else:
		return binary_search(data, target, mid_index  + 1, high_index)


if __name__ ==  '__main__':
	data = [random.randint(0, 100) for i in range(10)]
	data.sort()
	# para crear una lista ordenada sin modifcar los elementos de la lista
	# sorted_data = sorted(data)
	print(data)
	target = int(input("What number would you like to find? "))
	found = binary_search(data, target, 0, len(data) - 1)

	print(found)