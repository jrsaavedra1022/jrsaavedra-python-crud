import csv
import os

CLIENT_TABLE = 'Files/clients.csv'
CLIENT_SCHEMA = ['position', 'company', 'name', 'email']
clients = []


def _initialize_clients_from_storage():

    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

    os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the clients list')


def list_clients():
    global clients

    for idx, client in enumerate(clients):
        try:
            pass
            print('{uid} | {name} | {company} | {email} | {position}'.format(
                uid=idx,
                name=client['name'],
                company=client['company'],
                email=client['email'],
                position=client['position']
            ))
        except KeyError:
            pass


def update_client(client_name):
    global clients

    for client in clients:
        if client['name'] == client_name:

            client['name'] = _get_client_field('new name')
            client['company'] = _get_client_field('new company')
            client['email'] = _get_client_field('new email')
            client['position'] = _get_client_field('new position')

            list_clients()


def delete_client(client_name):
    global clients

    for client in clients:
        if client['name'] == client_name:
            del client['name']
            del client['company']
            del client['email']
            del client['position']


def search_client(client_mame):
    global clients

    for client in clients:
        if client['name'] != client_mame:
            continue
        else:
            return True


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))
    
    return field


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')
    print('[S]earch client')


if __name__ == '__main__':
    _initialize_clients_from_storage()
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':

        client ={
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }

        create_client(client)
        list_clients()

    elif command == 'D':

        client_name = _get_client_field('name')
        delete_client(client_name)
        list_clients()

    elif command == 'U':

        client_name = _get_client_field('name')
        update_client(client_name)

    elif command == 'S':

        client_name = _get_client_field('name')
        found = search_client(client_name)

        if found:
            print('The client is in the clients list')
        else:
            print('The client: {} is not in the clients list'.format(client_name))
    else:
        print('Invalid command')


    _save_clients_to_storage()