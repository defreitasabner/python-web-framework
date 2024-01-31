from controllers.base_controller import BaseController
from services.example_service import ExampleService


class ExampleController(BaseController):
    def __init__(self, service: ExampleService) -> None:
        self.service = service
        super().__init__()

    def response(self):
        print('Example Controller is working with service')