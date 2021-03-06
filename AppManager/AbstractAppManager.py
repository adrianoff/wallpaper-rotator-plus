import json
import os
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
        self.exec_path = None
        self._ui = UIManager()

        screen_resolution = self._ui.app.desktop().screenGeometry()
        self._source = AdrianovProSource(
            self.get_wallpaper_dir(),
            screen_resolution.width(),
            screen_resolution.height(),
            self.get_font_path()
        )

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
        return UpdateThread(self.update_wallpaper, 60*60*24)

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
            if os.path.exists(file_path):
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

    @abstractmethod
    def run_on_startup_trigger(self):
        pass

    @abstractmethod
    def is_run_on_startup(self):
        pass

    @abstractmethod
    def get_exec_file_path(self):
        pass

    @abstractmethod
    def get_font_path(self):
        pass
