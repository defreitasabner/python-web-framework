from injectors.controller_injector import ControllerInjector

def main():
    controllers = ControllerInjector.inject()
    controllers['example_controller'].response()

if __name__ == '__main__':
    main()