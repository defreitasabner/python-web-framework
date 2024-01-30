from pydoc import locate
import inspect

from controllers.example_controller import ExampleController

def main():
    # Injecting Controllers
    package_name = 'controllers'
    package = locate(package_name)
    all_modules = inspect.getmembers(package, inspect.ismodule)
    for module_name, module in all_modules:
        print(module_name)
        all_classes = inspect.getmembers(module, inspect.isclass)
        locals()[module_name] = all_classes[-1][1]()
    locals()['example_controller'].response()

if __name__ == '__main__':
    main()