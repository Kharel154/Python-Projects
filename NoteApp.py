

FILE = "myNote.txt"

def menu():
    print("\n---- Note Taking App Menu ----\n")
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Delete all notes")
    print("4. Exit")


def add_note():
    note = input("Enter your note : \n ")
    with open(FILE, "a") as file:
        file.write(note + "\n")
    print("Note added successfully")


def view_note():
    try:
        with open(FILE,"r") as file:
            content = file.read()
            if content:
                print("\n --- Your Notes ---")
                print(content)
            else:
                print("\n No notes found")
    except FileNotFoundError:
        print("No notes found.")


def delete_note():
    confirm = input("Ar you sure you want to delete all notes ? (yes/n) : ")
    if confirm.lower() == "yes":
        with open(FILE, "w") as file:
            pass
        print("All notes have been deleted")
    else:
        print("Deletion cancelled")


while True:
    menu()
    choice= input("Enter your choice : ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_note()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        print("Exiting Note-Taking App. Good Bye!")
        break
    else:
        print("Invalid choice ! Please retry \n")

