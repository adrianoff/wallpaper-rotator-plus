from AppManager.LinuxAppManager import LinuxAppManager


class Factory(object):
    _app_manager = None

    @staticmethod
    def get_app_manager():
        app_manager = LinuxAppManager()

        return app_manager
