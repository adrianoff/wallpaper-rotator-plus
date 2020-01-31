from AppManager.AbstractAppManager import AbstractAppManager
from AppManager.LinuxAppManager import LinuxAppManager
from AppManager.MacAppManager import MacAppManager
from AppManager.WindowsAppManager import WindowsAppManager
import platform


class Factory(object):
    _app_manager = None

    @staticmethod
    def get_app_manager() -> AbstractAppManager:
        os_platform = platform.system()
        if os_platform == 'Linux':
            app_manager = LinuxAppManager()
        elif os_platform == 'Windows':
            app_manager = WindowsAppManager()
        elif os_platform == 'Darwin':
            app_manager = MacAppManager()
        else:
            raise NotImplementedError('This platform not supported.')

        return app_manager
