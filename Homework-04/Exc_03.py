# items = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
# print(len(items))
# i = len(items) - 1
# print(i)
# if len(items) == 1:
#     print(items[0])
# ingredient_list = ", " .join(items[:-1]) + " and " + items[-1]
# print(ingredient_list)


def format_ingredients(items):
    if not items:
        return " "
    elif len(items) == 1:
        return items[0]
    else:
        ingredient_list = ", ".join(items[:-1])
        ingredient_list = f"{ingredient_list} and {items[-1]}"
    print(ingredient_list)


# print(format_ingredients(['a', 'b', 'c', 'd']))
format_ingredients(['a', 'b', 'c', 'd', 'e', 'f'])
