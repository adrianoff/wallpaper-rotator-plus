from Source.AbstractSource import AbstractSource
import requests
import json


class AdrianovProSource(AbstractSource):
    def __init__(self, wallpapers_dir, screen_width, screen_height):
        super().__init__(wallpapers_dir, screen_width, screen_height)

    def get_image_info(self):
        url = 'http://wrp.adrianov.pro/api/random/picture'
        req = requests.get(url, verify=False)
        result = json.loads(req.text)
        result['url'] = 'http://wrp.adrianov.pro/' + result['file']
        result['info_link'] = result['link_info']

        self.picture_name = result['name']
        self.painter_name = result['painter']

        return result
