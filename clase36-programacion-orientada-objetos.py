class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def say_hello(self):
		print("Hola mi nombre es: {} y mi edad es: {}".format(self.name, self.age))		



if __name__ == '__main__':
	person = Person('Jose', 20)
	print('Age: {}'.format(person.age))
	person.say_hello()