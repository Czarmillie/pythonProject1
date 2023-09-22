class DogException(Exception):
    def __int__(self, message: str) -> None:
        super().__init__(message)