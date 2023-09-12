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
    spicy_foods_name = []
    for i in range(len(spicy_foods)):
        spicy_foods_name += [value for key, value in spicy_foods[i].items() if key == 'name']
    return spicy_foods_name

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for i in range(len(spicy_foods)):
        spiciest_foods+=[spicy_foods[i] for key, value in spicy_foods[i].items() if key == 'heat_level' and value > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for i in range(len(spicy_foods)):
        print(f"{spicy_foods[i]['name']} ({spicy_foods[i]['cuisine']}) | Heat Level: {'🌶' * spicy_foods[i]['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_food_by_cuisine = []
    for i in range(len(spicy_foods)):
       spicy_food_by_cuisine += [spicy_foods[i] for key, value in spicy_foods[i].items() if key == 'cuisine' and value == cuisine]
    return spicy_food_by_cuisine[0]

def print_spiciest_foods(spicy_foods):
    for i in range(len(spicy_foods)):
        if spicy_foods[i]['heat_level'] > 5:
            print(f"{spicy_foods[i]['name']} ({spicy_foods[i]['cuisine']}) | Heat Level: {'🌶' * spicy_foods[i]['heat_level']}")

def get_average_heat_level(spicy_foods):
    total_heat = 0
    for i in range(len(spicy_foods)):
        total_heat += spicy_foods[i]['heat_level']
    average_heat_level = total_heat / len(spicy_foods)
    return int(average_heat_level)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods


create_spicy_food(spicy_foods, {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
})