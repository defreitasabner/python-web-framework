from injectors.controller_injector import ControllerInjector


def main():
    subpath = 'example'
    ControllerInjector.search(subpath)

if __name__ == '__main__':
    main()