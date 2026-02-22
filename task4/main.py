from handler import change_input, parse_input, add_contact, show_all, show_phone, show_commands
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            result = add_contact(args, contacts)
            print(result)
        elif command == "change":
            result = change_input(args, contacts)
            print(result)
        elif command == "all":
            result = show_all(contacts)
            print(result)
        elif command == "phone":
            result = show_phone(args, contacts)
            print(result)
        elif command == "help":
            print(show_commands())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

