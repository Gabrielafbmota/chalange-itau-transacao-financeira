from abc import ABC, abstractmethod
from typing import Optional
from entities.account import Account


class AccountRepositoryInterface(ABC):
    @abstractmethod
    def get_account(self, number: int) -> Optional[Account]:
        pass

    @abstractmethod
    def update_account(self, account: Account) -> None:
        pass
