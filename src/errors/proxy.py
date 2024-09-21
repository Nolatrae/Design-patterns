class ExceptionWrapper:
    __message: str = ""

    def __init__(self, exc: Exception = None):
        if exc is not None:
            self.__message = str(exc)

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, new_message: str) -> None:
        if new_message == "":
            raise ValueError("Message must not be empty!")
        self.__message = new_message

    @property
    def empty(self) -> bool:
        return len(self.__message) == 0
