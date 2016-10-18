from PyQt5.QtWidgets import QAction

import actions
from app import Factory


def main():
    app_manager = Factory.get_app_manager()

    exit_action = actions.create_exit_action(app_manager)
    app_manager.add_action_to_menu(exit_action)

    app_manager.init_dirs()
    app_manager.tray_icon.show()
    app_manager.app.exec_()

if __name__ == '__main__':
    main()
