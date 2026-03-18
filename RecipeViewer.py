

def loadrecipes(filepath):
    try:
        with open(filepath,"r") as file:
            content = file.read()
            recipes = content.split("\n\n")
            recipe_dict = {}
            for recipe in recipes:
                lines = recipe.split("\n")
                if len(lines) >= 3:
                    name = lines[0].strip()
                    ingredients = lines[1].replace('Ingredients: ','').strip()
                    instructions = lines[2].replace('Instructions: ','').strip()
                    recipe_dict[name] = {"ingredients": ingredients, "instructions": instructions}
            return recipe_dict
    except FileNotFoundError:
        print("File not found!")
        return{}



def menu():
    print("\n---- Reciepe Viewer Menu ----")
    print("1. View Recipe by Name")
    print("2. List all Recipes")
    print("3. Exit")



def view_recipe(recipes):
    name = input("Enter the name of the recipe: ").strip()
    if name in recipes:
        print(f"\n--- Recipe {name} Details ---")
        print(f"Ingredients: {recipes[name]['ingredients']}")
        print(f"Instructions: {recipes[name]['instructions']}")
    else:
        print("Recipe not found.")


recipe_file = "recipes.txt"
recipes = loadrecipes(recipe_file)

while True:
    menu()
    choice = input("Enter your choice : ")

    if choice == "1":
        view_recipe(recipes)
    elif choice == "2":
        print("\n---- All Recipes ----")
        for name in recipes:
            print(name)
    elif choice == "3":
        print("Exitin....")
        break
    else:
        print("Invalid choice. Retry")
