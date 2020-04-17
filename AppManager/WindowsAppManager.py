from AppManager.AbstractAppManager import AbstractAppManager
from WallpaperChanger.WindowsWallpaperChanger import WindowsWallpaperChanger
import os


class WindowsAppManager(AbstractAppManager):
    def __init__(self):
        self._wallpaper_changer = WindowsWallpaperChanger()
        super().__init__()

    @property
    def wallpaper_changer(self):
        return self._wallpaper_changer

    def init_dirs(self):
        if not os.path.exists(os.path.expanduser('~\\AppData\\LocalLow\\wallpaper-rotator-plus')):
            os.mkdir(os.path.expanduser('~\\AppData\\LocalLow\\wallpaper-rotator-plus'))

        if not os.path.exists(os.path.expanduser('~\\AppData\\LocalLow\\wallpaper-rotator-plus\\wallpapers')):
            os.mkdir(os.path.expanduser('~\\AppData\\LocalLow\\wallpaper-rotator-plus\\wallpapers'))
        pass

    def get_wallpaper_dir(self):
        return os.path.expanduser('~\\AppData\\LocalLow\\wallpaper-rotator-plus\\wallpapers')

    def get_dir(self):
        return os.path.expanduser('~\\AppData\\LocalLow\\wallpaper-rotator-plus')

    def change_wallpaper(self):
        wallpaper = self.source.get_current_wallpaper()
        self.wallpaper_changer.change_wallpaper(wallpaper)

    def run_on_startup_trigger(self):
        pass

    def is_run_on_startup(self):
        pass

    def get_exec_file_path(self):
        return self.exec_path + '\\artground.exe'