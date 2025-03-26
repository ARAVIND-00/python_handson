from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self,account_number,balance,acc_name):
        self._account_number=account_number
        self._balance=balance
        self._acc_name=acc_name

    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def get_account_info(self):
        pass

# class accountno(Account):
#     def w