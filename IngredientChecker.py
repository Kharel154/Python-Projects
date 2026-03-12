
ingredients = {"flour","sugar","butter","eggs","milk"}



user_input= input("Enter ingredients you have seperating them by , : ")
user_ing = set(user_input.split(", "))



missing_ing = ingredients - user_ing
extra_ing = user_ing - ingredients




print("\n---- Ingredients Check Results ----\n")
if missing_ing:
    print(f"You are missing the following ingredients : {', '.join(missing_ing)}")
else:
    print("You have all the ingredients needed.")

if extra_ing:
    print(f"You have extra ingredients: {', '.join(extra_ing)}")
else:
    print("You have all the ingredients needed.")
