from abc import ABC, abstractmethod


class AbstractWallpaperChanger(ABC):

    @abstractmethod
    def change_wallpaper(self, background):
        pass

