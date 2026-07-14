import sys

while(True):
    choice = None
    valid_choices = ["insert", "read", "exit"]

    while choice not in valid_choices:
        choice = input(f"enter a choice from {", ".join(valid_choices)}: ")
    
    if choice == "insert":
        name = input("enter name of student: ")
        address = input("enter address of student: ")
        contact = input("enter contact info of student: ")

        with open("data.txt", "a") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Contact: {contact}\n")

    if choice == "read":
        try:
            with open("data.txt", "r") as file:
                for line in file:
                    print(line)

        except Exception as e:
            print(f"Error: {e.args[1]}")

    if choice == "exit":
        sys.exit(0)