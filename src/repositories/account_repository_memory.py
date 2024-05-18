from typing import Dict, Optional
from entities.account import Account
from .account_repository_interface import AccountRepositoryInterface


class AccountRepositoryMemory(AccountRepositoryInterface):
    def __init__(self):
        self.accounts: Dict[int, Account] = {
            938485762: Account(938485762, 180),
            347586970: Account(347586970, 1200),
            2147483649: Account(2147483649, 0),
            675869708: Account(675869708, 4900),
            238596054: Account(238596054, 478),
            573659065: Account(573659065, 787),
            210385733: Account(210385733, 10),
            674038564: Account(674038564, 400),
            563856300: Account(563856300, 1200),
        }

    def get_account(self, number: int) -> Optional[Account]:
        return self.accounts.get(number)

    def update_account(self, account: Account) -> None:
        self.accounts[account.number] = account
