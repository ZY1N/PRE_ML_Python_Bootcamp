def printrecipe(item, cookbook):
    if(item in cookbook):
        print(f'Recipe for {item}')
        print(f'Ingredients list {cookbook[item]["ingredients"]}')
        print(f'To be eaten for {cookbook[item]["meal"]}.')
        print(f'Takes {cookbook[item]["prep_time"]} minutes of cooking.')
    else:
        print("Doesn't exist in Cookbook")

def deleteitem(item, cookbook):
    if(item in cookbook):
        del cookbook[item]
        print("Deleted")
    else:
        print("Doesn't exist in Cookbook")

def addrecipe(item, cookbook):
    ingredientlist = []
    name = input("What is the name of this food item?\n")
    while(1):
        ingredient = input("Please enter the ingredients, press x to finish\n")
        if(ingredient == "x"):
            break
        ingredientlist += ingredient
    meal = input("What meal is it eaten for?\n")
    prep_time = input("How long, in minutes, does it take to make?\n")
    cookbook[name] = {'ingredients':ingredientlist,
                    'meal': meal,
                    'prep_time': prep_time}

def main():
    cookbook = {
        'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                    'meal': 'lunch',
                    'prep_time': '10'},
        'cake': {'ingredients': ['flour', 'sugar', 'eggs'],
                'meal': 'desert',
                'prep_time': '60'},
        'salad': {'ingredients': ['avocado', 'tomatoes', 'spinach'],
                'meal': 'lunch', 
                'prep_time': '15'}
    }
    while(1):
        choice = input(
    """Please select an option by typing the corresponding number: 
1: Add a recipe 
2: Delete a recipe 
3: Print a recipe 
4: Print the cookbook 
5: Quit""")

    

if(__name__ == "__main__"):
    main()
