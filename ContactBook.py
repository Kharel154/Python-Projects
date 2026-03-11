#Dictionary 
contact = {}



def menu():
    print("----CONTACT BOOK MENU----")
    print("1) Add contact")
    print("2) View all contact")
    print("3) Search contact")
    print("4) Edit contact")
    print("5) Delete contact")
    print("6) Exit")
    



def Add_contact():
    name = input("Enter the name of your contact : ")
    phone = input("Enter the phone number : ")
    email = input("Enter the email : ")

    contact[name] = {"phone" : phone, "email" : email }

    print(f"{name}'s contact has been successfully added to your contact book \n")



def View_contact():
    
    if contact:
        print("\n ---Contact list---\n")
        i=0
        for name, details in contact.items():
            i=i+1
            print(f"{i} - name : {name} \n Phone : {details.get('phone')} \n email : {details.get('email')} ")
    else:
        print("No contact saved in the Contact book \n")



def Search_contact():
    name = input("Enter the name of the contact you want to search for in the contact book : ")
    if name in contact:
        print(f"-Name : {name} \n-Phone : {contact[name]['phone']}  \n-Email : {contact[name]['email']}\n ")
    else:
        print(f"Contact of {name} is not found in the contact book")


def Edit_contact():
    name = input("Enter the name of the contact you want to edit : ")
    if name in contact:
        phone = input("Enter the new phone numnber : ")
        email = input("Enter the new email : ")
        contact[name] = { "phone" : phone , "email" : email }
        print(f"The contact {name} has been successfully updated")
    else:
        print(f"The contact {name} is not found in the contact book")


def Delete_contact():
    name = input("Enter the name of the contact to delete : ")
    if name in contact:
        del contact[name]
        print(f" Contact {name} had been succesfully deleted")
    else:
        print(f"{name} not found in the contact book")




while True:
    menu()
    choice = input("Enter your choice : ")

    if choice == "1":
        Add_contact()
    elif choice == "2":
        View_contact()
    elif choice == "3":
        Search_contact()
    elif choice == "4":
        Edit_contact()
    elif choice == "5":
        Delete_contact()
    elif choice == "6":
        print("Good Bye !")
        break
    else:
        print("Invalid choice !")
    


