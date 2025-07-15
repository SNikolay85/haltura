from fastapi import APIRouter
from functions import search_post_vk


query_word = ['работ', 'ламинат', 'электрик', 'выключател', 'розетк', 'провод']
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

router = APIRouter(prefix='/start', tags=['Run'])


@router.get('/')
async def get_post():
    posts = search_post_vk(list_group, query_word)
    return posts

