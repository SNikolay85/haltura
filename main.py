import requests
from config import SERVICE_KEY, TOKEN_HH
from pprint import pprint
from datetime import datetime, timedelta
from time import time
import re


URL = 'https://api.vk.com/method/'
BASE_URL_HH = 'https://api.hh.ru/'
method_get = 'wall.get'
method_search = 'wall.search'
query_word = ['ламинат', 'электрик', 'выключател', 'розетк', 'провод']
list_group = [
    {'name': 'Шёпот Новосемейкино', 'domain': 'novosemeykino_shopot', 'owner_id': -94916453},
    {'name': 'Моё Новосемейкино', 'domain': 'my_novosemeykino', 'owner_id': -137533018},
    {'name': 'Самара и область Работа Подработка Халтура', 'domain': 'podrabotkasmr163', 'owner_id': -191601950},
    {'name': 'Шабашка Самара|Подработка|Услуги|Халтура', 'domain': 'shabashka163', 'owner_id': -171426949},
    {'name': 'Халтура Работа Самара | Услуги | Подработка', 'domain': 'rabota_haltura_samara', 'owner_id': -27545339},
    {'name': 'Моё Новосемейкино • Барахолка', 'domain': 'my_novosemeykino_market', 'owner_id': -159207210},
    {'name': 'В Яру(Красный ЯР, Самарская обл.)', 'domain': 'overheard_163', 'owner_id': -61489395},
    {'name': 'Подслушано | Самара', 'domain': 'overstory163', 'owner_id': -42949290},
    {'name': 'Халтура Самара | Работа', 'domain': 'nehaltura_samara', 'owner_id': -77521971}
]

# param={'access_token': SERVICE_KEY, 'domain': 'speshilove86', 'offset': 1, 'count': 2, 'v': 5.199}

#rec = requests.get(url=f'{URL}{method}', params=param).json()


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time()
        return_value = func(*args, **kwargs)
        end = time()
        print(f'[*] Время выполнения: {end - start} секунд.')
        return return_value
    return wrapper


@benchmark
def search_post_wall(parameter, query):
    param = {'access_token': SERVICE_KEY, 'domain': parameter['domain'], 'count': 20, 'v': 5.199}
    rec = requests.get(url=f'{URL}{method_get}', params=param).json()
    lst_wall = []
    date_need = datetime.now() - timedelta(3)
    for k in rec['response']['items']:
        list_query = sum(list(map(lambda x: re.findall(x, k['text'].lower()), query)), [])
        if datetime.fromtimestamp(k['date']).date() > date_need.date() and list_query != []:
            lst_wall.append(f"{datetime.fromtimestamp(k['date'])}, 'https://vk.com/wall{parameter['owner_id']}_{k['id']}'")
    return lst_wall


def search_post(parameter):
    param = {'access_token': SERVICE_KEY,
             'owner_id': parameter['owner_id'],
             'domain': parameter['domain'],
             'query': "ламинат",
             'count': 10,
             'v': 5.199}
    rec = requests.get(url=f'{URL}{method_search}', params=param).json()
    lst = []
    date_need = datetime.now() - timedelta(3)
    for k in rec['response']['items']:
        if datetime.fromtimestamp(k['date']).date() > date_need.date():
            lst.append(f"{datetime.fromtimestamp(k['date'])}, 'https://vk.com/wall{param['owner_id']}_{k['id']}'")
    return lst #f"{datetime.fromtimestamp(k['date'])}, 'https://vk.com/wall{param['owner_id']}_{k['id']}'"
    #return rec['response']['items'][0]['id']


# Функция для получения вакансий
def get_vacancies(city, vacancy, page):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'text': f'{vacancy} {city}',
        'area': city,
        'specialization': 1,
        'per_page': 100,
        'page': page
    }
    headers = {
        'Authorization': f'Bearer {TOKEN_HH}'
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


# for i in list_group:
#     print(i['name'])
#     pprint(search_post(i))


for i in list_group:
    result = search_post_wall(i, query_word)
    if result != []:
        print(i['name'])
        pprint(result)

#dd = datetime.fromtimestamp(date)

# pprint(len(rec['response']['items']))
# for i in rec['response']['items']:
#     print(datetime.fromtimestamp(i['date']), i['text'])
# pprint(rec['response']['items'])
