import uuid
from abc import ABC, abstractmethod


class IEntity(ABC):
    def __init__(self):
        self.__id = uuid.uuid4()

    @property
    def id(self):
        return self.__id

    @abstractmethod
    def local_equals(self, other):
        ...

    def __eq__(self, other):
        return self.id == other.id or self.local_equals(other)

