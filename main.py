import actions
from app import Factory
import threading
import qrc


def main():
    app_manager = Factory.get_app_manager()

    about_action = actions.create_about_action(app_manager)
    exit_action = actions.create_exit_action(app_manager)
    app_manager.add_action_to_menu(about_action)
    app_manager.add_separator_to_menu()
    app_manager.add_action_to_menu(exit_action)

    if not app_manager.source.is_current_image_exists():
        t = threading.Thread(target=app_manager.update_wallpaper)
        t.start()
    else:
        app_manager.change_wallpaper()

    app_manager.init_dirs()
    app_manager.tray_icon.show()
    app_manager.app.exec_()

if __name__ == '__main__':
    main()
