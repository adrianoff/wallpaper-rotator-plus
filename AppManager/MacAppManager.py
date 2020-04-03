from AppManager.LinuxAppManager import LinuxAppManager
from WallpaperChanger.MacWallpaperChanger import MacWallpaperChanger


class MacAppManager(LinuxAppManager):
    def __init__(self):
        super().__init__()
        self._wallpaper_changer = MacWallpaperChanger()

    @property
    def wallpaper_changer(self):
        return self._wallpaper_changer
