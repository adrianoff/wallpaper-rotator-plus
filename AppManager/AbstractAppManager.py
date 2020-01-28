import json
from abc import ABC
from abc import abstractmethod

from Source.AdrianovProSource import AdrianovProSource
from Threads.UpdateThread import UpdateThread
from UIManager.UIManager import UIManager

import webbrowser


class AbstractAppManager(ABC):
    def __init__(self):
        self.update_thread = self.create_thread()
        self._current_image_info = None
        self._source = AdrianovProSource(self.get_wallpaper_dir())
        self._ui = UIManager()
        self.update_current_image_info()

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
            self.ui.show_message('Error', "Can't download source picture.")

            return False

    def update_wallpaper(self):
        if self.download_picture():
            self.source.resize()
            self.change_wallpaper()
            self.save_current_image_info()

    def create_thread(self):
        return UpdateThread(self.update_wallpaper, 20)

    def restart_thread(self):
        if isinstance(self.update_thread, UpdateThread) and self.update_thread.is_alive():
            self.update_thread.done()

        self.update_thread = self.create_thread()
        self.update_thread.start()

    def start_thread(self):
        self.update_thread.start()

    def open_link(self):
        self.update_current_image_info()
        if \
                self._current_image_info is not None and \
                isinstance(self._current_image_info, dict) and \
                'info_link' in self._current_image_info.keys():

            webbrowser.open(self._current_image_info['info_link'])

    def save_current_image_info(self):
        file_path = self.get_dir() + '/current_image_info.json'
        with open(file_path, "w") as fp:
            json.dump(self._current_image_info, fp, indent=4, ensure_ascii=False)

    def update_current_image_info(self):
        if self._current_image_info is None:
            file_path = self.get_dir() + '/current_image_info.json'
            with open(file_path, "r") as fp:
                data = json.load(fp)
                keys = data.keys()
                if 'url' in keys and 'author' in keys and 'title' in keys and 'year' in keys and 'info_link' in keys:
                    self._current_image_info = data

    def exit_app(self):
        self.update_thread.done()
        self.ui.app.quit()

    @abstractmethod
    def change_wallpaper(self):
        pass

    @abstractmethod
    def init_dirs(self):
        pass

    @abstractmethod
    def get_wallpaper_dir(self):
        pass

    @abstractmethod
    def get_dir(self):
        pass
