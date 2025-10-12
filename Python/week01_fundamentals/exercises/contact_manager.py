""" Day 5 Practice Exericise: Contact Manager """

# Create a Contact Manager program:

# 1) Start with a list of contacts (names): ["Alice Smith", "Bob Jones", "Charlie Brown", "Diana Prince"]

# 2) Create these functions:
#       - format_contact(name) - Returns name in uppercase
#       - get_first_name(name) - Returns just the first name
#       - get_last_name(name) - Returns just the last name
#       - search_contacts(contacts, search_term) - Returns list of contacts containing the search term (case-insensitive)
#       - add_contact(contacts, name) - Adds a new contact and returns updates list
#       - remove_contact(contacts, name) - Removes a contact and returns updated list

# 3) Main program:
#       - Display all contacts (formatted)
#       - Search for contacts with "Brown" in the name
#       - Add a new contact "Eve Wilson"
#       - Remove "Bob Jones"
#       - Display final contact list with first and last names seperated

# Variables
names = ["Alice Smith", "Bob Jones", "Charlie Brown", "Diana Prince"]

# Functions
def format_contact(name):
    # Returns in uppercase
    return name.upper()

def get_first_name(name):
    # Returns just the first name
    word = name.split()
    return word[0]

def get_last_name(name):
    # Returns just the last name
    word = name.split()
    return word[-1]

def search_contacts(contacts, search_term):
    # Returns list of contacts containg the search term (case-insensitive)
    results = [contact for contact in contacts if search_term.lower() in contact.lower()]
    return results

def add_contact(contacts, name):
    # Adds a new contact and returns updates list
    contacts.append(name)
    return contacts

def remove_contact(contacts, name):
    # Removes a contact and returns updated list
    contacts.remove(name)
    return contacts

# Main program
print("=== All Contacts ===")
for name in names:
    print(format_contact(name))

print("\n=== Search Results for 'Brown' ===")
results = search_contacts(names, "Brown")
for contact in results:
    print(contact)

print("\n=== After Adding Eve Wilson === ")
names = add_contact(names, "Eve Wilson")
for name in names:
    print(format_contact(name))

print("\n=== After Removing Bob Jones ===")
names = remove_contact(names, "Bob Jones")
for name in names:
    print(format_contact(name))

print("\n=== Final Contact List (First & Last Names) ===")
for name in names:
    print(f"First: {get_first_name(name)}, Last: {get_last_name(name)}")
