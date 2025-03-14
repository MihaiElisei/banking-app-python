# Bank Account Management System

## Overview
This Python program simulates a banking system with different types of accounts, transactions, and error handling. It includes standard bank accounts, interest-earning accounts, and savings accounts with withdrawal fees.

## Features
- **Standard Bank Account**
  - Deposit and withdraw funds
  - Transfer funds between accounts
  - Prevent overdrafts using custom exceptions
- **Interest Rewards Account**
  - Deposits earn a 5% interest bonus
- **Savings Account**
  - Inherits interest rewards
  - Applies a withdrawal fee

## Example Output
```
Account 'Mihai' created.
Balance = $1000.00

Account 'Andrei' created.
Balance = $2000.00

Account 'Mihai' balance = $1000.00

Account 'Andrei' balance = $2000.00

Deposit complete.

Account 'Mihai' balance = $1500.00

Withdrawal complete!

Account 'Andrei' balance = $1900.00

**********

Beginning Transfer...🚀

Withdrawal complete!

Account 'Mihai' balance = $1450.00

Deposit complete.

Account 'Andrei' balance = $1950.00

Transfer complete! ✅

**********

Account 'Jim' created.
Balance = $1000.00

Account 'Jim' balance = $1000.00

Deposit complete (with interest bonus).

Account 'Jim' balance = $1105.00

**********

Beginning Transfer...🚀

Withdrawal complete!

Account 'Jim' balance = $1005.00

Deposit complete.

Account 'Mihai' balance = $1550.00

Transfer complete! ✅

**********

Account 'Ionut' created.
Balance = $1000.00

Account 'Ionut' balance = $1000.00

Deposit complete (with interest bonus).

Account 'Ionut' balance = $1105.00

**********

Beginning Transfer...🚀

Withdrawal complete (including fee).

Account 'Ionut' balance = $1090.00

Deposit complete.

Account 'Mihai' balance = $1560.00

Transfer complete! ✅

**********
```

## How to Use
1. Run the Python script.
2. Create accounts and perform transactions interactively.
3. Observe the real-time account updates and transaction logs.

## Notes
- Transfers and withdrawals will be blocked if the balance is insufficient.
- Interest rewards apply automatically upon deposits in the respective account types.
- The program ensures transactions are handled safely with error handling.
