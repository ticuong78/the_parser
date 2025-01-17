from abc import ABC, abstractmethod

class PreProcessor(ABC):
    @abstractmethod
    def preprocess(self, object: dict) -> dict:
        return