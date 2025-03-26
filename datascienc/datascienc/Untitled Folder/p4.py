from p3 import Account

class SavingsAccount (Account):
    def __init__(self,account_number,balance,acc_name,interest):
        super().__init__(account_number,balance,acc_name)
        self._interest=interest

    def deposit(self,amount):
        if amount>0:
            self._balance=self._balance+amount
            return f'Deposited ${amount}. New balance: ${self._balance}'
        else:
             return 'Deposit amount must be positive.'
        
    def withdraw(self,amount):
        if amount>0:
            if self._balance >= amount:
                self._balance=self._balance-amount
                return f'Withdrew ${amount}. New balance: ${self._balance}'
            else:
                return 'Insufficient funds.'
        else:
           return 'Withdrawal amount must be positive.'
        
    def get_balance(self):
        return self._balance
    
    def get_account_info(self):
       return f'Savings Account - {self._acc_name}, Account Number: {self._account_number}, Balance: ${self._balance}, Interest Rate: {self._interest * 100}%'

class CheckingAccount (Account):
    def __init__(self,account_number,balance,acc_name,over_draft):
        super().__init__(account_number,balance,acc_name)
        self._over_draft=over_draft

    def deposit(self,amount):
        if amount>0:
            self._balance=self._balance+amount
            return f'Deposited ${amount}. New balance: ${self._balance}'
        else:
             return 'Deposit amount must be positive.'
        
    def withdraw(self,amount):
        if amount>0:
            if self._balance  + self._over_draft >= amount:
                self._balance=self._balance-amount
                return f'Withdrew ${amount}. New balance: ${self._balance}'
            else:
                return 'Insufficient funds.'
        else:
           return 'Withdrawal amount must be positive.'
        
    def get_balance(self):
        return self._balance
    
    def get_account_info(self):
       return f'Checking Account - {self._acc_name}, Account Number: {self._account_number}, Balance: ${self._balance}, over_draft: {self._over_draft}'




def perform_operation(accounts):
    for account in accounts:
        print(account.get_account_info())
        print(account.deposit(100))
        print(account.withdraw(50))
        print(account.get_balance())
        print()


savingaccount=SavingsAccount(1234,100,'aravind',0.02)
checkingaccount=CheckingAccount(1234,900,'vijay',500)

accounts=[savingaccount,checkingaccount]

perform_operation(accounts)
