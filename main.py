# Задача №1

def grouping_into_a_dictionary():
    name_list = ['ingredient_name', 'quantity', 'measure']
    cook_book = {}
    with open('dish recipe', encoding='utf8') as recipes_file:
        for line in recipes_file:
            cook_book[line.strip()] = []
            quantity = int(recipes_file.readline())
            for i in range(quantity):
                items = {}
                ingredients = recipes_file.readline().strip().split(' | ')
                for x, y in zip(name_list, ingredients):
                    items[x] = y
                cook_book[line.strip()].append(items)
                items['quantity'] = int(items['quantity'])
            recipes_file.readline()
        return cook_book

# Задача №2

def get_shop_list_by_dishes(dishes, person_count):
    dishes_component = {}
    cook_book = grouping_into_a_dictionary()
    for dish in dishes:
        if dish not in cook_book.keys():
            print('Блюдо не найдено... Вы кто такие, я вас не звал, идите...')
            return
        for ingredients in cook_book[dish]:
            if ingredients['ingredient_name'] not in dishes_component:
                total_ingredients = {}
                ingredient_key = ingredients['ingredient_name']
                total_ingredients['measure'] = ingredients['measure']
                total_ingredients['quantity'] = ingredients['quantity'] * person_count
                dishes_component[ingredient_key] = total_ingredients
            else:
                dishes_component[ingredients['ingredient_name']]['quantity'] += ingredients['quantity'] * person_count
    print(dishes_component)

# Задача №3

def get_total_file(files):#В files передаётся список с желаемыми файлами
    zip_ = {}
    sorted_dict = {}
    for file in files:
        with open(file, encoding='utf8') as marked_file:
            len_list = []
            len_file = len(marked_file.readlines())
            len_list.append(len_file)
            zip_[file] = len_list
    sorted_keys = sorted(zip_, key=zip_.get)
    for w in sorted_keys:
        sorted_dict[w] = zip_[w]
    for x, y in sorted_dict.items():
        with open('final_file.txt', 'a', encoding='utf8') as f, open(x, 'r', encoding='utf8') as chosen_file:
            f.write(f'{x}\n'
                    f'{y}\n'
                    f'{" ".join(chosen_file.readlines())}\n')
