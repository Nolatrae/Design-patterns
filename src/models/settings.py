class Settings:
    # Поля с начальными значениями
    _inn = ""
    _account = ""
    _corr_account = ""
    _bik = ""
    _name = ""
    _ownership_type = ""

    # INN
    @property
    def inn(self):
        return self._inn

    @inn.setter
    def inn(self, value):
        if isinstance(value, str) and len(value) == 12:
            self._inn = value
        else:
            raise ValueError("ИНН должен быть строкой и содержать 12 символов.")

    # Счет
    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        if isinstance(value, str) and len(value) == 11:
            self._account = value
        else:
            raise ValueError("Счет должен быть строкой и содержать 11 символов.")

    # Корреспондентский счет
    @property
    def corr_account(self):
        return self._corr_account

    @corr_account.setter
    def corr_account(self, value):
        if isinstance(value, str) and len(value) == 11:
            self._corr_account = value
        else:
            raise ValueError("Корреспондентский счет должен быть строкой и содержать 11 символов.")

    # БИК
    @property
    def bik(self):
        return self._bik

    @bik.setter
    def bik(self, value):
        if isinstance(value, str) and len(value) == 9:
            self._bik = value
        else:
            raise ValueError("БИК должен быть строкой и содержать 9 символов.")

    # Наименование
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Наименование должно быть строкой.")

    # Вид собственности
    @property
    def ownership_type(self):
        return self._ownership_type

    @ownership_type.setter
    def ownership_type(self, value):
        if isinstance(value, str) and len(value) == 5:
            self._ownership_type = value
        else:
            raise ValueError("Вид собственности должен быть строкой и содержать 5 символов.")

    def __str__(self):
        return (f"ИНН: {self._inn}\n"
                f"Счет: {self._account}\n"
                f"Корреспондентский счет: {self._corr_account}\n"
                f"БИК: {self._bik}\n"
                f"Наименование: {self._name}\n"
                f"Вид собственности: {self._ownership_type}")