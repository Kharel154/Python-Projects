
def Cels_fahr(celsuis):
    return (celsuis * 9/5)+32

def Cels_kelv(celsuis):
    return celsuis + 273.15

def Fahr_cels(fahr):
    return (fahr - 32) * 5/9

def Fahr_kelv(fahr):
    return (fahr - 32) * 5/9 + 273.15

def Kelv_fahr(kelv):
    return (kelv - 273.15) * 9/5 + 32

def Kelv_cels(kelv):
    return kelv - 273.15

def menu():
    print("\n--- Temperature Converter Menu ---\n")
    print("1. Celsuis to Fahrenheit and Kelvin")
    print("2. Fahrenheit to Celsuis znd Kelvin")
    print("3. Kelvin to Celsuis and Fahrenheit")
    print("4. Exit")


while True:
    menu()
    choice = input("Enter your chooice : ")

    if choice == "1":
        cels=float(input("Enter the temperature in Celsuis : "))
        print(f"Fahrenheit : {Celc_fahr(cels) : .2f}")
        print(f"Kelvin : {Celc_kelv(cels) : .2f}")
    elif choice == "2":
        fahr=float(input("Enter the temperature in Fahrenheit : "))
        print(f"Celsuis : {Fahr_cels(fahr) : .2f}")
        print(f"Kelvin : {Fahr_kelv(fahr) : .2f}")
    elif choice == "3":
        kelv=float(input("Enter the temperature in Kelvin : "))
        print(f"Fahrenheit : {Kelv_fahr(kelv) : .2f}")
        print(f"Celsuis : {Kelv_cels(kelv) : .2f}")
    elif choice == "4":if choice == "1":
        print("Exiting......")
        break
    else:
