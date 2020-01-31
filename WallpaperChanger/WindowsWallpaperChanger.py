from WallpaperChanger.AbstractWallpaperChanger import AbstractWallpaperChanger
import ctypes


class WindowsWallpaperChanger(AbstractWallpaperChanger):

    def change_wallpaper(self, background):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, background, 0)
