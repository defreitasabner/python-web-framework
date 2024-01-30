from pydoc import locate
import inspect

from injectors.injector import Injector
from controllers import *


class ControllerInjector(Injector):
    @staticmethod
    def inject():
        package_name = 'controllers'
        package = locate(package_name)
        all_modules = inspect.getmembers(package, inspect.ismodule)
        controllers = dict()
        for module_name, module in all_modules:
            all_classes = inspect.getmembers(module, inspect.isclass)
            controllers[module_name] = all_classes[-1][1]()
        return controllers