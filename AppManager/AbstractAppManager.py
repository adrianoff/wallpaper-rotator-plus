from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QWidget
from Source.YandexFotkiSource import YandexFotkiSource


class AbstractAppManager(object):
    def __init__(self):
        self._app = QApplication([])

        QApplication.setQuitOnLastWindowClosed(False)

        self._q_icon = QtGui.QIcon("tray_icon.png")
        self._tray_icon = QSystemTrayIcon(self._q_icon, self._app)
        self._menu = QMenu()
        self._tray_icon.setContextMenu(self.menu)

        self._about_window = QWidget()
        self._about_window.setWindowTitle('About')
        self._about_window.resize(250, 150)
        self._about_window.move(300, 300)
        self._about_window.setFixedSize(250, 150)
        self._about_window.hide()

        self._source = YandexFotkiSource(self.get_wallpaper_dir())

    @property
    def app(self):
        return self._app

    @property
    def tray_icon(self):
        return self._tray_icon

    @property
    def menu(self):
        return self._menu

    @property
    def source(self):
        return self._source

    def add_action_to_menu(self, action):
        self._menu.addAction(action)

    def show_about_window(self):
        self._about_window.show()

    def download_picture(self):
        try:
            url = self.source.get_image_url()
            self.source.download_picture(url)

            return True
        except Exception:
            self.tray_icon.showMessage('Error', 'Can not download source picture.', self._q_icon)

            return False

    def update_wallpaper(self):
        if self.download_picture():
            self.source.resize()
            self.change_wallpaper()

    def change_wallpaper(self):
        raise NotImplementedError("Override this method please")

    def init_dirs(self):
        raise NotImplementedError("Override this method please")

    def get_wallpaper_dir(self):
        raise NotImplementedError("Override this method please")
