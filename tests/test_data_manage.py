import pytest

from utils import data_manage
import os

test_file = os.path.join('tests', 'test_operations.json')
expected_raw_list = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2023-08-01T10:50:58.294041",
        "operationAmount": {
            "amount": "123.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
    {
    },
    {
        "id": 41428829,
        "state": "CANCELLED",
        "date": "2023-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "to": "Счет 35383033474447895560"
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "1990-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Mastercard 1596837868705199",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2023-01-30T10:45:06.972075",
        "operationAmount": {
            "amount": "48223.05",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2022-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }
]
expected_extracted_data = [
    ["2023-08-01", "Перевод организации", "Maestro 1596837868705199", "Счет 64686473678894779589", "123.58", "руб."],
    ["1990-06-30", "Перевод организации", "Visa Mastercard 1596837868705199", "Счет 11776614605963066702", "9824.07",
     "USD"],
    ["2023-01-30", "Открытие вклада", "N/A", "Счет 41421565395219882431", "48223.05", "руб."],
    ["2022-04-04", "Перевод со счета на счет", "Счет 19708645243227258542", "Счет 75651667383060284188", "79114.93",
     "USD"]
]
expected_sorted_list = [
    ["2023-08-01", "Перевод организации", "Maestro 1596837868705199", "Счет 64686473678894779589", "123.58", "руб."],
    ["2023-01-30", "Открытие вклада", "N/A", "Счет 41421565395219882431", "48223.05", "руб."],
    ["2022-04-04", "Перевод со счета на счет", "Счет 19708645243227258542", "Счет 75651667383060284188", "79114.93",
     "USD"],
    ["1990-06-30", "Перевод организации", "Visa Mastercard 1596837868705199", "Счет 11776614605963066702", "9824.07",
     "USD"],
]


def test_load_data():
    assert data_manage.load_data(test_file) == expected_raw_list


def test_extract_data():
    assert data_manage.extract_data(expected_raw_list) == expected_extracted_data


def test_sort_list():
    assert data_manage.sort_list(expected_extracted_data) == expected_sorted_list


def test_format_date():
    assert data_manage.format_date('2015-12-04') == '04.12.2015'


@pytest.mark.parametrize('account, expected', [
    ('Счет 43241152692663622869', 'Счет **2869'),
    ('Счет 0043241152692663622869', 'неизвестный формат счета/карты'),
    ('Visa Classic 2842878893689012', 'Visa Classic 2842 87** **** 9012'),
    ('Maestro 2842878893689012', 'Maestro 2842 87** **** 9012'),
    ('Maestro 2842878893689o12', 'неизвестный формат счета/карты'),
    ('N/A', 'N/A')
])
def test_mask_account(account, expected):
    assert data_manage.mask_account(account) == expected
