from controllers.base_controller import BaseController

class ExampleController(BaseController):
    def __init__(self) -> None:
        super().__init__()

    def response(self):
        print('Example Controller is working')