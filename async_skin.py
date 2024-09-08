'''
@author     :nianwei100
@contact    :2297709907@qq.com
@file       :async_skin.py
@desc       :fetch lol hero's skins
'''
import asyncio
import os
from time import perf_counter

import aiohttp
import requests
from fake_useragent import UserAgent
from loguru import logger

start = perf_counter()
# global variable
ROOT_DIR = os.path.dirname(__file__)
os.mkdir(f'{ROOT_DIR}/image')
IMG_DIR = f'{ROOT_DIR}/image'
RIGHT = 0  # counts of right image
ERROR = 0  # counts of error image
headers = {'User-Agent': UserAgent().random}
# target url
HERO_URL = 'http://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
# skin's url, will completed with hero's id.
BASE_URL = 'http://game.gtimg.cn/images/lol/act/img/js/hero/'
loop = asyncio.get_event_loop()
tasks = []


def get_hero_id(target_url):
    '''
    get hero's id, to complete base_url.
 
    :param url: target url
    :return: hero's id
    '''
    response = requests.get(url=target_url, headers=headers, timeout=60)
    info = response.json()
    items = info.get('hero')
    for item in items:
        yield item.get('heroId')


async def fetch_hero_url(hero_url):
    '''
    fetch hero url, to get skin's info
 
    :param url: hero url
    :return: None
    '''
    async with aiohttp.ClientSession() as session:
        async with session.get(url=hero_url, headers=headers) as response:
            if response.status == 200:
                response = await response.json(
                    content_type='application/x-javascript')
                # skin's list
                skins = response.get('skins')
                for skin in skins:
                    info = {}
                    info['hero_name'] = skin.get('heroName') + '_' + skin.get(
                        'heroTitle')
                    info['skin_name'] = skin.get('name')
                    info['skin_url'] = skin.get('mainImg')
                    await fetch_skin_url(info)


async def fetch_skin_url(info):
    '''
    fetch image, save it to jpg.
 
    :param info: skin's info
    :return: None
    '''
    global RIGHT, ERROR
    path = f'{IMG_DIR}/{info["hero_name"]}'
    make_dir(path)
    name = info['skin_name']
    exec_url = info['skin_url']
    if name.count('/'):
        name.replace('/', '//')
    elif exec_url == '':
        ERROR += 1
        logger.error(f'{name} url error {ERROR}')
    else:
        RIGHT += 1
        async with aiohttp.ClientSession() as session:
            async with session.get(url=exec_url, headers=headers) as response:
                if response.status == 200:
                    with open(f'{path}/{name}.jpg', 'wb') as file:
                        chunk = await response.content.read()
                        logger.success(f'download {name} right {RIGHT}...')
                        file.write(chunk)
                else:
                    ERROR += 1
                    logger.error(f'{name},{exec_url} status!=200')


def make_dir(path):
    '''
    make dir with hero's name
 
    :param path: path
    :return: None
    '''
    if not os.path.exists(path):
        os.mkdir(path)


if __name__ == '__main__':
    for hero_id in get_hero_id(HERO_URL):
        URL_ = BASE_URL + str(hero_id) + '.js'
        tasks.append(fetch_hero_url(URL_))
    loop.run_until_complete(asyncio.wait(tasks))
    logger.info(f'count times {perf_counter() - start}s')
    logger.info(f'download RIGHT {RIGHT}, download ERROR {ERROR}')
