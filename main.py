with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        meal = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for _ in range(ingredients_count):
            ing = file.readline().strip()
            ingredients_name, quantity, measure = ing.split(" | ")
            ingredients.append(
                {'ingredient_name': ingredients_name,
                 'quantity': quantity,
                 'measure': measure}
            )
        cook_book[meal] = ingredients
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    total = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                if ingr['ingredient_name'] in total.keys():
                    total[ingr['ingredient_name']]['quantity'] += int(ingr['quantity']) * person_count
                else:
                    total[ingr['ingredient_name']] = {'measure': ingr['measure'],
                                                       'quantity': int(ingr['quantity']) * person_count}
    return total


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))