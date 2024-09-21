from src.interfaces.baseEntity import IEntity


class Warehouse(IEntity):
    def local_equals(self, other):
        ...

