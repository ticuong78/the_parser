from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def _parse(self):
        pass