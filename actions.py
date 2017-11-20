from PyQt5.QtWidgets import QAction


def create_exit_action(app_manager):
    exit_action = QAction()
    exit_action.setText("Exit")
    exit_action.setShortcut('Ctrl+Q')
    exit_action.setStatusTip('Exit application')
    exit_action.triggered.connect(app_manager.app.quit)

    return exit_action


def create_about_action(app_manager):
    exit_action = QAction()
    exit_action.setText("About")
    exit_action.triggered.connect(app_manager.show_about_window)

    return exit_action