#Passwoerd generator

import random, string

passwordlist = []

try:
    with open('GenPassword.txt','r') as f:
        for lign in f:
            passwordlist.append(lign.strip())
except FileNotFoundError:
   print("Will load new password list") 


def pass_gen(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    specialchars = "!@*$:;,?./£µ%§<>≤≥^]}`|[{#~ˇ"

    password = [
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(digits),
            random.choice(specialchars)
            ]

    all_chars = uppercase + lowercase + digits + specialchars
    password += random.choices(all_chars, k=length-4)

    random.shuffle(password)

    return ''.join(password)


while True:
    print("\n--- Password Generator Menu ---\n")
    print("1. Generate password")
    print("2. See generated passwords")
    print("3. Exit")
    ch = input("Enter your choice : ")

    if ch == "1":
        try:
            length = int(input("Enter a password length greater than 4 : "))
            num = int(input("How many passwords do you want to generate ? : "))
            for i in range(num):
                password = pass_gen(length)
                print("Generated Password : ", password)
                passwordlist.append(password)
        except ValueError as e:
            print(e)

    elif ch == "2":
        if not passwordlist:
            print("No password generated previously !")
        else:
            for i, pas in enumerate(passwordlist):
                print(f"{i+1}-{pas}")

    elif ch == "3":
        f = open('GenPassword.txt','w')
        for i in range(len(passwordlist)):
            f.write(f'{passwordlist[i]} \n')
        print("Good Bye !")
        break

    else:
        print("Invalid Entry ! Retry\n")
