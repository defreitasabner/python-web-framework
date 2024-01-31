from pydoc import locate
import inspect

from injectors.injector import Injector


class ControllerInjector(Injector):
    @staticmethod
    def search(subpath):
        package_name = 'controllers'
        package = locate(package_name)
        all_modules = inspect.getmembers(package, inspect.ismodule)
        controller_module = list(filter(lambda module: True if module[0].startswith(subpath) else False, all_modules))[0][1]
        all_classes = inspect.getmembers(controller_module, inspect.isclass)
        controller = list(filter(lambda cls: True if cls[1].__module__ == controller_module.__name__ else False, all_classes))[0][1]
        print(controller)