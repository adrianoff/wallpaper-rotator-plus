import re

import bs4
import requests

from Source.AbstractSource import AbstractSource


class YandexFotkiSource(AbstractSource):
    def __init__(self, wallpapers_dir):
        super().__init__(wallpapers_dir)

    def get_image_url(self):
        base_url = 'http://fotki.yandex.ru'
        html1 = requests.get(base_url).text
        parser = bs4.BeautifulSoup(html1, 'lxml')
        a = parser.find('a', attrs={'class': 'photo-well-image photo-well-image_pod photo-well-image_is-visible'})
        href1 = a['href']

        html2 = requests.get(base_url + href1).text
        a = re.search(r'(?<=\,\"x5l\"\:\{\"url\"\:\")(.*)(?=X5L)', html2)
        img_src = a.group(0) + '_X5L'

        return img_src