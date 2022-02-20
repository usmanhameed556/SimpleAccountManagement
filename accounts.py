import datetime
import pytz


class Account:
    """simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        # self.transaction_list = []
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for \n" + self._name)
        # print("The account has the amount",+ self.balance)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("the amount must be greater")
        self.show_balance()

    def show_balance(self):
        print("your account balance is {} ".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {}  (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    usman = Account('Usman', 500)
    # usman.show_balance()

    usman.deposit(1000)
    usman.withdraw(800)
    usman.withdraw(9000)
    usman.show_transactions()
    usman.show_balance()
    # open another person bank account
    waqas = Account('Waqas', 800)
    waqas.__balance = 200
    waqas.deposit(200)
    waqas.withdraw(100)
    waqas.show_transactions()
    waqas.show_balance()
    print(waqas.__dict__)
    waqas._Account__balance = 40
    waqas.show_balance()


