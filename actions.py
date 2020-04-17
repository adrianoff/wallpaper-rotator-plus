from PyQt5.QtWidgets import QAction
from AppManager import AbstractAppManager


def create_exit_action(app_manager: AbstractAppManager):
    exit_action = QAction()
    exit_action.setText("Exit")
    exit_action.setShortcut('Ctrl+Q')
    exit_action.setStatusTip('Exit application')
    exit_action.triggered.connect(app_manager.exit_app)

    return exit_action


def create_open_link_action(app_manager: AbstractAppManager):
    open_link_action = QAction()
    open_link_action.setText("Read Info")
    open_link_action.triggered.connect(app_manager.open_link)

    return open_link_action


def create_next_action(app_manager: AbstractAppManager):
    next_action = QAction()
    next_action.setText("Next")
    next_action.triggered.connect(app_manager.restart_thread)

    return next_action


def create_about_action(app_manager: AbstractAppManager):
    exit_action = QAction()
    exit_action.setText("About")
    exit_action.triggered.connect(app_manager.ui.show_about_window)

    return exit_action


def create_run_on_startup_action(app_manager: AbstractAppManager):
    run_on_startup_action = QAction()
    run_on_startup_action.setText("Run on startup")
    run_on_startup_action.setCheckable(True)
    run_on_startup_action.setChecked(app_manager.is_run_on_startup())
    run_on_startup_action.triggered.connect(app_manager.run_on_startup_trigger)

    return run_on_startup_action
