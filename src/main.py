from injectors.controller_injector import ControllerInjector

if __name__ == '__main__':
    controllers = ControllerInjector.inject()
    controllers['example_controller'].response()