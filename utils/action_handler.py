from abc import ABC, abstractmethod

class AbstractActionHandler(ABC):
    @abstractmethod
    def handle(self, message):
        pass