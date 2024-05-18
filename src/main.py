from services.transfer_service import TransferService
from repositories.account_repository_memory import AccountRepositoryMemory

TRANSACTIONS = [
    {
        "correlation_id": 1,
        "datetime": "09/09/2023 14:15:00",
        "origin_account": 938485762,
        "destination_account": 2147483649,
        "AMOUNT": 150,
    },
    {
        "correlation_id": 2,
        "datetime": "09/09/2023 14:15:05",
        "origin_account": 2147483649,
        "destination_account": 210385733,
        "AMOUNT": 149,
    },
    {
        "correlation_id": 3,
        "datetime": "09/09/2023 14:15:29",
        "origin_account": 347586970,
        "destination_account": 238596054,
        "AMOUNT": 1100,
    },
    {
        "correlation_id": 4,
        "datetime": "09/09/2023 14:17:00",
        "origin_account": 675869708,
        "destination_account": 210385733,
        "AMOUNT": 5300,
    },
    {
        "correlation_id": 5,
        "datetime": "09/09/2023 14:18:00",
        "origin_account": 238596054,
        "destination_account": 674038564,
        "AMOUNT": 1489,
    },
    {
        "correlation_id": 6,
        "datetime": "09/09/2023 14:18:20",
        "origin_account": 573659065,
        "destination_account": 563856300,
        "AMOUNT": 49,
    },
    {
        "correlation_id": 7,
        "datetime": "09/09/2023 14:19:00",
        "origin_account": 938485762,
        "destination_account": 2147483649,
        "AMOUNT": 44,
    },
    {
        "correlation_id": 8,
        "datetime": "09/09/2023 14:19:01",
        "origin_account": 573659065,
        "destination_account": 675869708,
        "AMOUNT": 150,
    },
]

if __name__ == "__main__":
    account_repository = AccountRepositoryMemory()
    transfer_service = TransferService(account_repository)

    for transaction in TRANSACTIONS:
        transfer_service.transfer(
            transaction["correlation_id"],
            transaction["origin_account"],
            transaction["destination_account"],
            transaction["AMOUNT"],
        )
