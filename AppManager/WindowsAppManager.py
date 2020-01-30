from AppManager.AbstractAppManager import AbstractAppManager
import os


class WindowsAppManager(AbstractAppManager):
    def __init__(self):
        super().__init__()

    def init_dirs(self):
        pass

    def get_wallpaper_dir(self):
        return os.path.expanduser('~/')

    def get_dir(self):
        return os.path.expanduser('~/')

    def change_wallpaper(self):
        pass
