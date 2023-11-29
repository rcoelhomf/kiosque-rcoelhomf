from menu import products


def calculate_tab(dict_list: list):

    total = 0

    for i in dict_list:
        for j in products:
            if j['_id'] == i['_id']:
                total = total + j['price'] * i['amount']

    return {'subtotal': f'${round(total, 2)}'}
