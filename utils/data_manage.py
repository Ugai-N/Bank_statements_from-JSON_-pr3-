import json
from datetime import date


def load_data(file):
    '''Выгружает данные из файла json'''
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


def extract_data(raw_list):
    '''Перекладывает выборочные данные по успешным сделкам в новый список'''
    filtered_list = []
    for i in raw_list:
        if 'state' in i.keys() and i['state'] == 'EXECUTED':
            i = [
                i.get('date')[:10],
                i.get('description'),
                i.get('from', 'N/A'),
                i.get('to'),
                i.get('operationAmount').get('amount'),
                i.get('operationAmount').get('currency').get('name')
            ]
            filtered_list.append(i)
    return filtered_list


def sort_list(filtered_list):
    '''Сортирует список операций по дате (последние сверху) и выгружает последние 5 операций'''
    sorted_list = sorted(filtered_list, reverse=True)
    return sorted_list[:5]


def format_date(operation_date):
    '''Форматирует дату по шаблону "21.12.2001"'''
    formatted_date = date.fromisoformat(operation_date).strftime("%d.%m.%Y")
    return formatted_date


def mask_account(account):
    '''Маскирует номер карты по шаблону XXXX XX** **** XXXX,
    Максирует номер счета по шаблону **XXXX (только последние 4 цифры)
    Выводит название карты/счета и замаскированный номер'''
    if account == "N/A":
        return "N/A"
    else:
        num = account.split(' ')[-1]
        if len(num) == 16 and num.isdigit():
            masked_num = f'{num[:4]} {num[4:6]}** **** {num[12:16]}'
            return account.replace(num, masked_num)
        elif len(num) == 20 and num.isdigit():
            masked_num = f'**{num[-4:]}'
            return account.replace(num, masked_num)
        else:
            return 'неизвестный формат счета/карты'
