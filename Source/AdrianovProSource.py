from Source.AbstractSource import AbstractSource


class AdrianovProSource(AbstractSource):
    def __init__(self, wallpapers_dir):
        super().__init__(wallpapers_dir)

    def get_image_info(self):
        return {
            'url': 'https://upload.wikimedia.org/wikipedia/commons/c/c9/Avtoportret_Gelyi_Korzev.jpg',
            'author': 'Гелий Коржев',
            'title': 'Название картины',
            'year': '1961',
            'info_link': 'https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%80%D0%B6%D0%B5%D0%B2,_%D0%93%D0%B5%D0%BB%D0%B8%D0%B9_%D0%9C%D0%B8%D1%85%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2%D0%B8%D1%87'
        }
