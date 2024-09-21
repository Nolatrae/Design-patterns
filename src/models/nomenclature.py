from src.interfaces.baseEntity import IEntity


class Nomenclature(IEntity):
    __name: str = ""
    __group = None
    __unit = None

    def __init__(self):
        super().__init__()

    def local_equals(self, other):
        return self.name == other.name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name