from AppManager.AbstractAppManager import AbstractAppManager
import os


class LinuxAppManager(AbstractAppManager):
    def __init__(self):
        super(LinuxAppManager, self).__init__()

    def init_dirs(self):
        if not os.path.exists(os.path.expanduser('~/.wallpaper-rotator-plus')):
            os.mkdir(os.path.expanduser('~/.wallpaper-rotator-plus'))

        if not os.path.exists(os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers')):
            os.mkdir(os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers'))

    def get_wallpaper_dir(self):
        return os.path.expanduser('~/.wallpaper-rotator-plus/wallpapers')