from WallpaperChanger.AbstractWallpaperChanger import AbstractWallpaperChanger
import os


class LinuxWallpaperChanger(AbstractWallpaperChanger):

    def change_wallpaper(self, background):
        command1 = ''.join(
            ["gsettings set org.gnome.desktop.background picture-options 'centered'"])
        command2 = ''.join(
            ["gsettings set org.gnome.desktop.background picture-uri file://", background])

        os.system(command1)
        os.system(command2)
