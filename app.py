from AppManager.AbstractAppManager import AbstractAppManager
from AppManager.LinuxAppManager import LinuxAppManager
from AppManager.WindowsAppManager import WindowsAppManager
import platform


class Factory(object):
    _app_manager = None

    @staticmethod
    def get_app_manager() -> AbstractAppManager:
        if platform.system() == 'Linux':
            app_manager = LinuxAppManager()
        elif platform.system() == 'Windows':
            app_manager = WindowsAppManager()
        else:
            raise NotImplementedError('This platform not supported.')

        return app_manager
