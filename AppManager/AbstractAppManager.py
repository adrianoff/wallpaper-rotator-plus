from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu


class AbstractAppManager(object):
    def __init__(self):
        self._app = QApplication([])
        self._tray_icon = QSystemTrayIcon(QtGui.QIcon("tray_icon.png"), self._app)
        self._menu = QMenu()
        self._tray_icon.setContextMenu(self.menu)

    @property
    def app(self):
        return self._app

    @property
    def tray_icon(self):
        return self._tray_icon

    @property
    def menu(self):
        return self._menu

    def add_action_to_menu(self, action):
        self._menu.addAction(action)

    def init_dirs(self):
        raise NotImplementedError("Override this method please")