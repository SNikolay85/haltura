import requests
from config import SERVICE_KEY
from datetime import datetime, timedelta
from time import time
import re


URL = 'https://api.vk.com/method/'
method_get = 'wall.get'


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


def search_post_vk(groups, words):
    list_request = []
    for i in groups:
        result = search_post_wall(i, words)
        if result != []:
            list_request.append({'name': i['name'], 'link': result})
    return list_request
