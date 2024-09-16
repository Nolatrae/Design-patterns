from src.models.settings import Settings
from src.interfaces.baseEntity import IEntity


class Organization(IEntity):
    """ Модель организации """

    def local_equals(self, other):
        return self.inn == other.inn

    __inn: str = ""
    __bik: str = ""
    __account: str = ""
    __ownership_type: str = ""

    def __init__(self, settings: Settings):
        super().__init__()
        self.__inn = settings.inn
        self.__bik = settings.bik
        self.__account = settings.account
        self.__ownership_type = settings.ownership_type

    def __str__(self):
        return f"inn: {self.__inn} \nbic: {self.__bik} \naccount: {self.__account} \ntype_of_ownership: {self.__ownership_type}"

    @property
    def inn(self):
        return self.__inn

    @property
    def bik(self):
        return self.__bik

    @property
    def account(self):
        return self.__account

    @property
    def ownership_type(self):
        return self.__ownership_type

