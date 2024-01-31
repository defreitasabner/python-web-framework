from controllers.base_controller import BaseController
from services.example_service import ExampleService
from auto_inject import auto_inject


class ExampleController(BaseController):
    def __init__(self, service: ExampleService = None) -> None:
        super().__init__()

    def response(self):
        print('Example Controller is working')