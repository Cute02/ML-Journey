# 1. Define the custom exception
class InsufficientFundsError(Exception):
    """Exception raised when an account has insufficient funds."""
    pass

# 2. Raise the custom exception


def withdraw_money(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(
            f"Cannot withdraw ${amount}. Balance is only ${balance}.")
    return balance - amount


# 3. Handle the custom exception
try:
    withdraw_money(balance=00, amount=150)
except InsufficientFundsError as e:
    print(f"Transaction Failed: {e}")
else:
    print("Transaction successful")
