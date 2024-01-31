from abc import ABC, abstractmethod
from typing import get_type_hints, Any

class Injector(ABC):
    @abstractmethod
    def search():
        pass

    @staticmethod
    def auto_inject(function) -> Any:
        def wrapper(*args, **kwargs):
            cls = function(*args, **kwargs)
            required_args = get_type_hints(cls.__init__)
            injection = {}
            for arg in list(required_args.keys()):
                if arg != 'return':
                    injection[arg] = required_args[arg]()
            return cls(**injection)
        return wrapper