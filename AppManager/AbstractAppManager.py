from abc import ABC
from abc import abstractmethod

from Source.AdrianovProSource import AdrianovProSource
from UIManager.UIManager import UIManager

import webbrowser


class AbstractAppManager(ABC):
    def __init__(self):
        self._current_image_info = None
        self._source = AdrianovProSource(self.get_wallpaper_dir())
        self._ui = UIManager()

    @property
    def ui(self):
        return self._ui

    @property
    def source(self):
        return self._source

    def download_picture(self):
        try:
            info = self.source.get_image_info()
            self.source.download_picture(info['url'])
            self._current_image_info = info

            return True
        except Exception:
            self.ui.show_message('Error', 'Can not download source picture.')

            return False

    def update_wallpaper(self):
        if self.download_picture():
            self.source.resize()
            self.change_wallpaper()

    def open_link(self):
        webbrowser.open(self._current_image_info['info_link'])

    @abstractmethod
    def change_wallpaper(self):
        pass

    @abstractmethod
    def init_dirs(self):
        pass

    @abstractmethod
    def get_wallpaper_dir(self):
        pass
