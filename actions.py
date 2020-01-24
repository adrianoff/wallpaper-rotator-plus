from PyQt5.QtWidgets import QAction
from AppManager import AbstractAppManager


def create_exit_action(app_manager: AbstractAppManager):
    exit_action = QAction()
    exit_action.setText("Exit")
    exit_action.setShortcut('Ctrl+Q')
    exit_action.setStatusTip('Exit application')
    exit_action.triggered.connect(app_manager.app.quit)

    return exit_action


def create_open_link_action(app_manager: AbstractAppManager):
    open_link_action = QAction()
    open_link_action.setText("Read Info")
    open_link_action.triggered.connect(app_manager.open_link)

    return open_link_action


def create_next_action(app_manager: AbstractAppManager):
    next_action = QAction()
    next_action.setText("Next")
    next_action.triggered.connect(app_manager.update_wallpaper)

    return next_action


def create_about_action(app_manager: AbstractAppManager):
    exit_action = QAction()
    exit_action.setText("About")
    exit_action.triggered.connect(app_manager.show_about_window)

    return exit_action