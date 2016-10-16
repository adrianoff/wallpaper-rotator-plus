from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction


class AbstractAppManager(object):
    def __init__(self):
        pass

    def create_app(self):
        app = QApplication([])

        tray_icon = QSystemTrayIcon(QtGui.QIcon("tray_icon.png"), app)

        exit_action = QAction()
        exit_action.setText("Exit")
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(app.quit)

        menu = QMenu()
        menu.addAction(exit_action)
        tray_icon.setContextMenu(menu)

        tray_icon.show()
        app.exec_()

        return app

    def init_dirs(self):
        raise NotImplementedError("Override this method please")