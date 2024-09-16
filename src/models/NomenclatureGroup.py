from src.interfaces.baseEntity import IEntity


class GroupNomenclature(IEntity):
    __nomenclature_type = ""

    def __init__(self):
        super().__init__()

    def local_equals(self, other):
        ...

    @staticmethod
    def create_base_group():
        return GroupNomenclature()