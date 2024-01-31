from injectors.controller_injector import ControllerInjector


def main():
    subpath = 'example'
    controller = ControllerInjector.search(subpath)
    controller.response()

if __name__ == '__main__':
    main()