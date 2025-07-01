from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def create_phone(self):
        pass

    @abstractmethod
    def create_charger(self):
        pass