from AppManager.AbstractAppManager import AbstractAppManager
from AppManager.LinuxAppManager import LinuxAppManager


class Factory(object):
    _app_manager = None

    @staticmethod
    def get_app_manager() -> AbstractAppManager:
        app_manager = LinuxAppManager()

        return app_manager
