from abc import ABC, abstractmethod

class Injector(ABC):
    @abstractmethod
    def inject():
        pass