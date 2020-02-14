# Decoradores de python ...
PASSWORD = '12345'

def passwoord_required(func):
	def wrapper():
		password = input("Cuál es la contraseña? ")
		if password == PASSWORD:
			return func()
		else:
			print("La contraseña NO es correcta.")

	return wrapper

@passwoord_required
def needs_password():
	print('La contraseña es correcta')

def upper(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		return result.upper()

	return wrapper

@upper
def say_my_name(name):
	return "Hola, {}".format(name)


if __name__ == '__main__':
	# needs_password()
	saludo = say_my_name("Jose ...")
	print(saludo)