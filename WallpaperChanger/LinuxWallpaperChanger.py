from WallpaperChanger import AbstractWallpaperChanger
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gio


class LinuxWallpaperChanger(AbstractWallpaperChanger):
    def change_wallpaper(self, background):
        schema = 'org.gnome.desktop.background'
        key = 'picture-uri'
        gio_settings = Gio.Settings.new(schema)
        gio_settings.set_string(key, "file://" + background)
