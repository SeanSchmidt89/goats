import os
import hashlib
import json

class PasswordManager:
    def __init__(self):
        self.passwords_file = 'passwords.json'
        self.passwords = self.load_passwords()

    def load_passwords(self):
        try:
            with open(self.passwords_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_passwords(self):
        with open(self.passwords_file, 'w') as file:
            json.dump(self.passwords, file, indent=4)

    def add_password(self, website, username, password):
        if website in self.passwords:
            print(f"Password for {website} already exists. Updating password...")
        self.passwords[website] = {'username': username, 'password': self.hash_password(password)}
        self.save_passwords()
        print(f"Password for {website} added/updated successfully!")

    def get_password(self, website):
        if website in self.passwords:
            return self.passwords[website]['password']
        else:
            print(f"No password found for {website}")
            return None

    def hash_password(self, password):
        # Using SHA-256 hashing algorithm
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

def main():
    password_manager = PasswordManager()

    while True:
        print("\n1. Add/Update Password\n2. Get Password\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            website = input("Enter website name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            password_manager.add_password(website, username, password)
        elif choice == '2':
            website = input("Enter website name: ")
            hashed_password = password_manager.get_password(website)
            if hashed_password:
                print(f"Password for {website}: {hashed_password}")
        elif choice == '3':
            print("Exiting Password Manager...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
