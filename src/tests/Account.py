from tests import InvalidAmountException, InsufficientAmountException


class Account:
    def __init__(self, first_name, last_name, account_number, pin):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__account_number = account_number
        self.__pin = pin
        self.__balance = 0


    def deposit(self, amount):
        if amount < 0:
            raise InvalidAmountException("Invalid Amount")
        else:
            self.__balance += amount
        return self.__balance


    def withdraw(self, amount, pin):
        if amount > 0:
            self.__validate_pin(pin)
            self.__amount_greater(amount)

            self.__balance -= amount

        else:
            return InsufficientAmountException("Insufficient Funds")

    def get_account_name(self):
        return self.__first_name and self.__last_name

    def get_account_number(self):
        return self.__account_number

    def get_balance(self, pin):
        if self.__validate_pin(pin):
            return self.__balance
        else:
            raise InsufficientAmountException("Incorrect Pin, Please try again: ")

    def __validate_pin(self, pin):
        if self.__pin == pin:
            return True
        else:
            raise InsufficientAmountException("Incorrect Pin, Please try again: ")

    def __amount_greater(self, amount):
        if amount > self.__balance:
            raise InsufficientAmountException("Insufficient Funds")