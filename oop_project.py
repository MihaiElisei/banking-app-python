from bank_accounts import *

Mihai = BankAccount(1000, "Mihai")
Andrei = BankAccount(2000, "Andrei")

Mihai.get_balance()
Andrei.get_balance()

Mihai.deposit(500)

Andrei.withdraw(100)

Mihai.transfer(50, Andrei)

Jim = InterestRewardsAccount(1000, "Jim")
Jim.get_balance()
Jim.deposit(100)

Jim.transfer(100, Mihai)

Ionut = SavingsAccount(1000, "Ionut")
Ionut.get_balance()
Ionut.deposit(100)
Ionut.transfer(10, Mihai)