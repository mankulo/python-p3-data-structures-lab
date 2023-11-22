spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    string_names = [food.get("name") for food in spicy_foods]
    return string_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods
    if food.get("heat_level") > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    
    for food in spicy_foods:
        result = ""
        name = food.get("name")
        cuisine = food.get("cuisine")
        heat_level = food.get("heat_level")
        heat_level_emoji = "🌶" * heat_level
        result += f"{name} ({cuisine}) | Heat Level: {heat_level_emoji}"
        print(result)
        
print(print_spicy_foods(spicy_foods))


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food



def print_spiciest_foods(spicy_foods):

    for food in spicy_foods:
        
        result = ""
        name = food.get("name")
        cuisine = food.get("cuisine")
        heat_level = food.get("heat_level")
        if heat_level > 5 :
           heat_level_emoji = "🌶" * heat_level
           result += f"{name} ({cuisine}) | Heat Level: {heat_level_emoji}"
           print(result)






def get_average_heat_level(spicy_foods):
    total_heat = sum((food.get("heat_level") for food in spicy_foods))
    length_of_food = len(spicy_foods)
    average_heat_level = total_heat / length_of_food
    return average_heat_level





def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
