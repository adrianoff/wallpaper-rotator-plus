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

    def get_dir(self):
        return os.path.expanduser('~/.wallpaper-rotator-plus')

    def change_wallpaper(self):
        wallpaper = self.source.get_current_wallpaper()
        self.wallpaper_changer.change_wallpaper(wallpaper)

    def run_on_startup_trigger(self):
        if self.is_run_on_startup():
            os.remove(os.path.expanduser('~/.config/autostart/artground.desktop'))
        else:
            lines = [
                '[Desktop Entry]',
                'Type=Application',
                'Exec="%s"' % self.get_exec_file_path(),
                'Hidden=false',
                'NoDisplay=false',
                'X-GNOME-Autostart-enabled=true',
                'Name=artground'
            ]
            with open(os.path.expanduser('~/.config/autostart/artground.desktop'), "w") as file:
                file.writelines("%s\n" % line for line in lines)
                file.close()

    def is_run_on_startup(self):
        return os.path.exists(os.path.expanduser('~/.config/autostart/artground.desktop'))

    def get_exec_file_path(self):
        return self.exec_path + '/artground'

    def get_font_path(self):
        return '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
