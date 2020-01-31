from AppManager.LinuxAppManager import LinuxAppManager
from WallpaperChanger.MacWallpaperChanger import MacWallpaperChanger


class MacAppManager(LinuxAppManager):
    def __init__(self):
        self._wallpaper_changer = MacWallpaperChanger()
        super().__init__()

    @property
    def wallpaper_changer(self):
        return self._wallpaper_changer
