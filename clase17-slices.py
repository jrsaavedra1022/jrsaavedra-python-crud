
word = 'reconocer'
long_word = 'ferrocarril'

print("palabra: {}".format(word))
print("primeras 3 letras: {}".format(word[:3]))
print("cuente 3 espacios hasta el final: {}".format(word[3:]))
# :: del inicio al final
print("palabra de dos en dos: {}".format(word[::2]))

print("palabra de dos en dos: {}".format(word[3:3]))
print("desde el principio: {}".format(word[:]))
print("el primero al ultimas de dos en dos: {}".format(word[1:-1:2]))

print("palabra larga: {}".format(long_word))
print("Empiece en 1 y termine en 4: {}".format(long_word[1:4]))
print("palabra de dos en dos: {}".format(word[3:3]))
print("De atras hacia adelante: {}".format(long_word[::-1]))
print("Principio al final de dos en dos: {}".format(long_word[::2]))

