print("Reto de binary serach ...")

import random

def binary_search(data, target, low, high):
	found = False
	while True:		
		print("Low: {}   High: {}".format(low, high))
		if low > high:
			break
		
		mid = (low + high) // 2
		if target == data[mid]:
			found = True
			break
		if target < data[mid]:
			high = mid - 1
		else:
			low = mid + 1

	return found

if __name__ ==  '__main__':
	data = [random.randint(0, 100) for i in range(10)]
	data.sort()
	# para crear una lista ordenada sin modifcar los elementos de la lista
	# sorted_data = sorted(data)
	print(data)
	target = int(input("What number would you like to find? "))
	found = binary_search(data, target, 0, len(data) - 1)

	print(found)