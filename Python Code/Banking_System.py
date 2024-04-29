import csv
import os

class BankSystem:
    def __init__(self):
        self.customers = {}
        self.load_data()

    def load_data(self):
        if os.path.exists('customer_data.csv'):
            with open('customer_data.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.customers[row['Customer ID']] = {
                        'name': row['Name'],
                        'email': row['Email'],
                        'phone_number': row['Phone Number'],
                        'address': row['Address'],
                        'balance': float(row['Balance']),
                        'username': row['Username'],
                        'password': row['Password']
                    }

    def save_data(self):
        with open('customer_data.csv', 'w', newline='') as file:
            fieldnames = ['Customer ID', 'Name', 'Email', 'Phone Number', 'Address', 'Balance', 'Username', 'Password']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for customer_id, info in self.customers.items():
                writer.writerow({
                    'Customer ID': customer_id,
                    'Name': info['name'],
                    'Email': info['email'],
                    'Phone Number': info['phone_number'],
                    'Address': info['address'],
                    'Balance': info['balance'],
                    'Username': info['username'],
                    'Password': info['password']
                })

    def generate_customer_id(self):
        if not self.customers:
            return '5139000001'
        else:
            return str(int(max(self.customers.keys())) + 1)

    def create_account(self, name, email, phone_number, address, initial_deposit, username, password):
        if email in [info['email'] for info in self.customers.values()]:
            print("Customer account already exists for the given email.")
            return
        elif phone_number in [info['phone_number'] for info in self.customers.values()]:
            print("Customer account already exists for the given phone number.")
            return

        customer_id = self.generate_customer_id()
        self.customers[customer_id] = {
            'name': name,
            'email': email,
            'phone_number': phone_number,
            'address': address,
            'balance': initial_deposit,
            'username': username,
            'password': password
        }
        self.save_data()
        print("Account created successfully! Your Customer ID is:", customer_id)

    def login(self, username, password):
        for customer_id, info in self.customers.items():
            if info['username'] == username and info['password'] == password:
                return customer_id
        return None

    def deposit(self, customer_id, amount):
        self.customers[customer_id]['balance'] += amount
        self.save_data()
        print("Amount deposited successfully.")

    def withdraw(self, customer_id, amount):
        if self.customers[customer_id]['balance'] >= amount:
            self.customers[customer_id]['balance'] -= amount
            self.save_data()
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_account_info(self, customer_id):
        info = self.customers[customer_id]
        print("Customer ID:", customer_id)
        print("Name:", info['name'])
        print("Email:", info['email'])
        print("Phone Number:", info['phone_number'])
        print("Address:", info['address'])

    def display_balance(self, customer_id):
        print("Your balance is:", self.customers[customer_id]['balance'])

    def close_account(self, customer_id):
        del self.customers[customer_id]
        self.save_data()
        print("Account closed successfully.")
