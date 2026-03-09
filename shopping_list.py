
shop_list = []

def menu():
    print("-------Menu-------")
    print("1. Display the list ")
    print("2. Add an item to the list")
    print("3. Remove an item from the list")
    print("4. Clear the list")
    print("5. Quit ")

while True:
    menu()
    choice=input("Enter a number from 1-5 : ")

    if choice == "1" :
        print("\n ---Shopping List--- \n")
        if not shop_list :
            print("The shopping list is empty!\n")
        else:
            for index,item in enumerate(shop_list):
                print(f"{index + 1}-{item}")
            print("\n\n")    
        
    elif choice == "2" :
        item = input("Enter your item name's : ")
        shop_list.append(item)
        print(f"\n {item} has been succesfuly added to the shopping list!\n")

    elif choice == "3" :
        item =input("\n Enter the item's name to remove from the lsit : ")
        if item in shop_list :
            shop_list.remove(item)
            print(f"\n {item} has been succesfuly removed rom the shopping list\n")
        else:
            print(f"\n {item} is not found in the shopping list \n")
    
    elif choice == "4" :
        shop_list.clear()
        print("\n List deleted succesfuly\n")
    

    elif choice == "5" :
        print("\n Good Bye !\n")
        break
    
    else:
        print("Wrong entry")
