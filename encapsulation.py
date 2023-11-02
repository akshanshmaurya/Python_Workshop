# Encaptulation:-
# Encaptulation is a concept taht restricts access to certain point of an object.
# In python you can mark members as private (by a double underscore prefix).
# in the "encaptulation" example,we create bankaccount classs .

#encaptulation example 
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
    def get_balance(self):
        return self._balance

account1 = BankAccount("12345", 1000)
print(account1._account_number)
print(account1.get_balance())        