import os
import platform

import actions
from app import Factory
import qrc

if platform.system() == 'Windows':
    import pkg_resources.py2_warn


def main():
    app_manager = Factory.get_app_manager()

    about_action = actions.create_about_action(app_manager)
    run_on_startup_action = actions.create_run_on_startup_action(app_manager)
    next_action = actions.create_next_action(app_manager)
    open_link_action = actions.create_open_link_action(app_manager)
    exit_action = actions.create_exit_action(app_manager)

    app_manager.ui.add_action_to_menu(about_action)
    app_manager.ui.add_action_to_menu(run_on_startup_action)
    app_manager.ui.add_separator_to_menu()
    app_manager.ui.add_action_to_menu(next_action)
    app_manager.ui.add_action_to_menu(open_link_action)
    app_manager.ui.add_separator_to_menu()
    app_manager.ui.add_action_to_menu(exit_action)

    app_manager.exec_path = os.path.dirname(os.path.abspath(__file__))
    app_manager.init_dirs()
    app_manager.update_current_image_info()
    app_manager.ui.tray_icon.show()
    app_manager.start_thread()
    app_manager.ui.app.exec_()


if __name__ == '__main__':
    main()
