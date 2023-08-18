from abc import ABC, abstractclassmethod

class Ilist(ABC):

    @abstractclassmethod
    def list(self, page: int):
        pass