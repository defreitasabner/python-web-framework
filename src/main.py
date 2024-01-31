from injectors.controller_injector import ControllerInjector


def main():
    path = '/example/response'
    subpaths = path.replace('/', '', 1).split('/')
    controller = ControllerInjector.search(subpaths[0])
    allowed_members = filter(lambda member: not member.startswith('__') and callable(getattr(controller, member)), dir(controller))
    if subpaths[1] in allowed_members:
        method = getattr(controller, subpaths[1])
        method()
    else:
        raise Exception('Method not found')

if __name__ == '__main__':
    main()