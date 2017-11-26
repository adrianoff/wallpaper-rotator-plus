from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.uic import loadUi
from Source.YandexFotkiSource import YandexFotkiSource


class AbstractAppManager(object):
    def __init__(self):
        self._app = QApplication([])

        QApplication.setQuitOnLastWindowClosed(False)

        self._q_icon = QtGui.QIcon("./Form/image/tray_icon.png")
        self._tray_icon = QSystemTrayIcon(self._q_icon, self._app)
        self._menu = QMenu()
        self._tray_icon.setContextMenu(self.menu)

        about_widget = loadUi("./Form/about.ui")
        self._about_window = about_widget
        self._about_window.setWindowTitle('About Wallpaper Rotator Plus')
        self._about_window.setWindowIcon(self._q_icon)
        about_width = 348
        about_height = 530
        self._about_window.resize(about_width, about_height)
        self._about_window.setFixedSize(about_width, about_height)
        self._about_window.aboutCloseButton.clicked.connect(self._about_window.hide)
        self._about_window.hide()

        center_point = QDesktopWidget().availableGeometry().center()
        center_point.setX(center_point.x() - int(about_width/2))
        center_point.setY(center_point.y() - int(about_height/2))
        self._about_window.move(center_point)

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

    def add_separator_to_menu(self):
        self._menu.addSeparator()

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
