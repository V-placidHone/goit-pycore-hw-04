def parse_input(user_input):
#does work if input is "add John 1234567890" 

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_input(args, contacts ):
#does work if input is "add John 1234567890" 
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."
    
def show_all(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."
        
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found."
    

def show_commands():
    return """Available commands:
    - hello: Greet the assistant bot.
    - add <name> <phone>: Add a new contact.
    - change <name> <phone>: Update an existing contact's phone number.
    - all: Show all contacts.
    - phone <name>: Show the phone number of a specific contact.
    - close/exit: Exit the assistant bot."""