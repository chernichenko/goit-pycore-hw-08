import pickle

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        self.contacts = [c for c in self.contacts if c.name != name]

    def save_data(self, filename="addressbook.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self.contacts, f)

    def load_data(self, filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                self.contacts = pickle.load(f)
        except FileNotFoundError:
            self.contacts = []

    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")

# Приклад використання
def main():
    address_book = AddressBook()
    address_book.load_data()

    while True:
        print("Address Book Menu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            contact = Contact(name, email, phone)
            address_book.add_contact(contact)

        elif choice == '2':
            name = input("Enter name to remove: ")
            address_book.remove_contact(name)

        elif choice == '3':
            address_book.display_contacts()

        elif choice == '4':
            address_book.save_data()
            break

if __name__ == "__main__":
    main()
