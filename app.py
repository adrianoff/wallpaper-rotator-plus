from AppManager.LinuxAppManager import LinuxAppManager


class Factory(object):
    @staticmethod
    def get_app_manager():
        app_manager = LinuxAppManager()

        return app_manager
