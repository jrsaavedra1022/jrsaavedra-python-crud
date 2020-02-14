import csv
import os

from clients.models import Client

class ClientService:


	def __init__(self, table_name):
		self.table_name = table_name


	def create_client(self, client):
		with open(self.table_name, mode='a', newline='') as f:
			writer = csv.DictWriter(f, fieldnames=Client.schema())
			writer.writerow(client.to_dict())

	def list_clients(self):
		with open(self.table_name, mode='r') as f:
			reader = csv.DictReader(f, fieldnames=Client.schema())

			return list(reader)

	def update_client(self, update_client):
		clients = self.list_clients()
		update_clients = []
		for client in clients:
			if client['uid'] == update_client.uid:
				update_clients.append(update_client.to_dict())
			else:
				update_clients.append(client)

		self._save_to_disk(update_clients)

	def delete_client(self, delete_client_uid):
		clients = self.list_clients()
		delete_clients = []
		for client in clients:
			if client['uid'] == delete_client_uid:
				continue
			else:
				delete_clients.append(client)

		self._save_to_disk(delete_clients)

	def _save_to_disk(self, clients):
		tmp_table_name = self.table_name + '.tmp'
		with open(tmp_table_name, mode="w", newline="") as f:
			writer = csv.DictWriter(f, fieldnames=Client.schema())
			writer.writerows(clients)

		os.remove(self.table_name)
		os.rename(tmp_table_name, self.table_name)