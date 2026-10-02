class Node:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None


class ContactList:
    def __init__(self):
        self.head = None

    def add_contact(self, name, phone):
        new_node = Node(name, phone)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

        print("Contact added successfully!")

    def display_contacts(self):
        if self.head is None:
            print("No contacts found.")
            return

        temp = self.head

        print("\n--- CONTACT LIST ---")

        while temp is not None:
            print("Name :", temp.name)
            print("Phone:", temp.phone)
            print("--------------------")
            temp = temp.next

    def search_contact(self, name):
        temp = self.head

        while temp is not None:
            if temp.name.lower() == name.lower():
                print("\nContact Found!")
                print("Name :", temp.name)
                print("Phone:", temp.phone)
                return
            temp = temp.next

        print("Contact not found.")

    def delete_contact(self, name):
        temp = self.head
        previous = None

        while temp is not None:
            if temp.name.lower() == name.lower():

                if previous is None:
                    self.head = temp.next
                else:
                    previous.next = temp.next

                print("Contact deleted successfully!")
                return

            previous = temp
            temp = temp.next

        print("Contact not found.")


contacts = ContactList()

while True:

    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts.add_contact(name, phone)

    elif choice == "2":
        contacts.display_contacts()

    elif choice == "3":
        name = input("Enter name to search: ")
        contacts.search_contact(name)

    elif choice == "4":
        name = input("Enter name to delete: ")
        contacts.delete_contact(name)

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice! Please enter 1 to 5.")