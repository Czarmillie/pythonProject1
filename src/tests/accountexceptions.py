class InvalidAmountException(Exception):
    def __int__(self, message):
        super().__init__(message)


class InsufficientAmountException(Exception):
    def __int__(self, message):
        super().__int__((message))