from AppManager.AbstractAppManager import AbstractAppManager
from WallpaperChanger.LinuxWallpaperChanger import LinuxWallpaperChanger
import os


class LinuxAppManager(AbstractAppManager):
    def __init__(self):
        self._wallpaper_changer = LinuxWallpaperChanger()
        super().__init__()

    @property
    def wallpaper_changer(self):
        return self._wallpaper_changer

    def init_dirs(self):
        if not os.path.exists(os.path.expanduser('~/.wallpaper-rotator-plus')):
            os.mkdir(os.path.expanduser('~/.wallpaper-rotator-plus'))

        if not os.path.exists(os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers')):
            os.mkdir(os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers'))

    def get_wallpaper_dir(self):
        return os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers')

    def change_wallpaper(self):
        wallpaper = self.source.get_current_wallpaper()
        self.wallpaper_changer.change_wallpaper(wallpaper)
