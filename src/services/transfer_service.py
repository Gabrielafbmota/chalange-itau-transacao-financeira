from repositories.account_repository_interface import AccountRepositoryInterface


class TransferService:
    def __init__(self, account_repository: AccountRepositoryInterface):
        self.account_repository = account_repository

    def transfer(
        self,
        correlation_id: int,
        origin_account: int,
        destination_account: int,
        amount: float,
    ) -> None:
        origin_account = self.account_repository.get_account(origin_account)
        if not origin_account:
            print(
                f"Transaction number {correlation_id} was canceled due to non-existent origin account"
            )
            return
        if origin_account.balance < amount:
            print(
                f"Transaction number {correlation_id} was canceled due to insufficient funds"
            )
            return

        destination_account = self.account_repository.get_account(destination_account)
        if not destination_account:
            print(
                f"Transaction number {correlation_id} was canceled due to non-existent destination account"
            )
            return

        origin_account.balance -= amount
        destination_account.balance += amount
        self.account_repository.update_account(origin_account)
        self.account_repository.update_account(destination_account)
        print(
            f"Transaction number {correlation_id} was successful! New balances: Origin Account:{origin_account.balance} | Destination Account: {destination_account.balance}"
        )
