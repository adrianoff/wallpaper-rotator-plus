from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.uic import loadUi
import qrc

from Form.about import AboutForm


class UIManager:

    def __init__(self):
        self._app = QApplication([])

        QApplication.setQuitOnLastWindowClosed(False)

        self._q_icon = QtGui.QIcon(":/image/image/tray_icon.png")
        self._tray_icon = QSystemTrayIcon(self._q_icon, self._app)
        self._menu = QMenu()
        self._tray_icon.setContextMenu(self.menu)

        #about_widget = loadUi("./Form/about.ui")

        about_widget = QtWidgets.QWidget()
        ui = AboutForm()
        ui.setupUi(about_widget)

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
        center_point.setX(center_point.x() - int(about_width / 2))
        center_point.setY(center_point.y() - int(about_height / 2))
        self._about_window.move(center_point)

    @property
    def app(self):
        return self._app

    @property
    def menu(self):
        return self._menu

    @property
    def tray_icon(self):
        return self._tray_icon

    def add_action_to_menu(self, action):
        self._menu.addAction(action)

    def add_separator_to_menu(self):
        self._menu.addSeparator()

    def show_about_window(self):
        self._about_window.show()

    def show_message(self, message_type, message):
        self.tray_icon.showMessage(message_type, message, self._q_icon)
