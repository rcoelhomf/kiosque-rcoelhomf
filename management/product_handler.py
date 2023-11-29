from menu import products


def get_product_by_id(id: int):

    if type(id) != int:
        raise TypeError('product id must be an int')

    dictionary = {}

    for i in products:
        if i['_id'] == id:
            dictionary = i

    return dictionary


def get_products_by_type(type_name: str):

    if type(type_name) != str:
        raise TypeError('product type must be a str')

    list = []

    for i in products:
        if i['type'] == type_name:
            list.append(i)

    return list


def add_product(menu: list, **kwargs: dict):

    new_id = 1

    for i in menu:
        if i['_id'] > new_id:
            new_id = i['_id'] + 1

    kwargs['_id'] = new_id
    menu.append(kwargs)

    return kwargs


def menu_report():

    count = 0

    total = 0

    all_types = []

    most_type = 0

    for i in products:
        count = count + 1
        total = total + i['price']
        data = all_types.count(i['type'])
        if data == 0:
            all_types.append(i['type'])

    for i in all_types:
        count_type = 0
        for j in products:
            if i == j['type']:
                count_type = count_type + 1

        if count_type > most_type:
            most_type = count_type
            most_common_type = i

    average_price = round(total / count, 2)

    return (
        f'Products Count: {count} - Average Price: ${average_price} - Most Common Type: {most_common_type}'
    )
