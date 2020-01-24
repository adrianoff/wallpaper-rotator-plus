from Source.AbstractSource import AbstractSource


class AdrianovProSource(AbstractSource):
    def __init__(self, wallpapers_dir):
        super().__init__(wallpapers_dir)

    def get_image_url(self):
        return 'https://artchive.ru/res/media/img/orig/article/798/323188@2x.jpg'