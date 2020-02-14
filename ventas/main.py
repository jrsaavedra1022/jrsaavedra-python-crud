import sys

clients = [
	{
		'name': 'Pablo',
		'company': 'Google',
		'email': 'pablo@google.com',
		'position': 'Software engineer',
	},
	{
		'name': 'Ricardo',
		'company': 'Facebook',
		'email': 'ricardo@facebook.com',
		'position': 'Data engineer',
	}

]

def create_client(client):
	global clients

	if client not in clients:
		clients.append(client)
	else:
		print("Client already is in the client's list")


def list_clients():
	for idx, client in enumerate(clients):
		print('{uid} | {name} | {company} | {email} | {position}'.format(
				uid=idx,
				name=client['name'],
				company=client['company'],
				email=client['email'],
				position=client['position']

			))


def update_client(client_id, updated_client):
	global clients

	if len(clients) - 1 >= client_id:
		clients[client_id] = updated_client
	else:
		print("Client is not in clients list")


def delete_client(client_id):
	global clients

	for idx, client in enumerate(clients):
		if idx == client_id:
			del clients[idx]
			break
	else:
		print("Client is not in client list")


def search_client(client_name):
	global clients

	for client in clients:
		if client['name'].upper() != client_name.upper():
			continue
		else:
			return True



def _print_welcome():
	print("Bienvenidos a Platzi ventas")
	print('*' * 50)
	print('What would you like to do today?')
	print('[C}reate client')
	print('[L}ist client')
	print('[U}pdate client')
	print('[D}elete client')
	print('[S}earch client')


def _get_client_field(field_name):
	field = None

	while not field:
		field = str(input("What is the client {}? ".format(field_name)))

		if field.upper() == 'EXIT':
			field = None
			break
	if not field:
		sys.exit()

	return field


def _get_client_from_user():
	client = {
			'name': _get_client_field('name'),
			'company': _get_client_field('company'),
			'email': _get_client_field('email'),
			'position': _get_client_field('position'),
	}

	return client


def _get_client_name():
	client_name = None
	while not client_name: 
		client_name = str(input("What is the client name? "))

		if client_name.upper() == "EXIT":
			client_name = None
			break

	if not client_name:
		sys.exit()

	return client_name


if __name__ == '__main__':
	_print_welcome()
	command = str(input(""))
	command = command.upper()

	if command == 'C':
		client =  _get_client_from_user()
		create_client(client)
		list_clients()

	elif command == 'L':
		list_clients()

	elif command == 'U':
		client_id = int(_get_client_field('id'))
		udpated_client =  _get_client_from_user()
		update_client(client_id, udpated_client)
		list_clients()

	elif command == 'D':
		client_id = int(_get_client_field('id'))
		delete_client(client_id)
		list_clients()

	elif command == 'S':
		client_name = _get_client_field('name')
		found = search_client(client_name)

		if found:
			print("The client is in the client's list")
		else:
			print("The client: {} is not in our client's list".format(client_name))

	else:
		print('Invalid command')


