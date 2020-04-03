from Source.AbstractSource import AbstractSource
import requests
import json


class AdrianovProSource(AbstractSource):
    def __init__(self, wallpapers_dir):
        super().__init__(wallpapers_dir)

    def get_image_info(self):
        url = 'http://localhost:8000/api/random/picture'
        req = requests.get(url, verify=False)
        result = json.loads(req.text)
        result['url'] = 'http://localhost:8000/' + result['file']
        result['info_link'] = result['link_info']

        return result
