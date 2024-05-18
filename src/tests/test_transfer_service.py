import unittest
from unittest.mock import patch
from entities.account import Account
from repositories.account_repository_memory import AccountRepositoryMemory
from services.transfer_service import TransferService


class TestTransferService(unittest.TestCase):
    def setUp(self):
        self.account_repository = AccountRepositoryMemory()
        self.transfer_service = TransferService(self.account_repository)

    @patch("builtins.print")
    def test_transfer_successful(self, mock_print):
        origin_account = self.account_repository.get_account(938485762)
        destination_account = self.account_repository.get_account(2147483649)

        self.transfer_service.transfer(1, 938485762, 2147483649, 100)

        self.assertEqual(origin_account.balance, 80)
        self.assertEqual(destination_account.balance, 100)
        mock_print.assert_called_with(
            "Transaction number 1 was successful! New balances: Origin Account:80 | Destination Account: 100"
        )

    @patch("builtins.print")
    def test_transfer_insufficient_funds(self, mock_print):
        self.transfer_service.transfer(2, 938485762, 2147483649, 200)
        mock_print.assert_called_with(
            "Transaction number 2 was canceled due to insufficient funds"
        )

    @patch("builtins.print")
    def test_transfer_non_existent_origin_account(self, mock_print):
        self.transfer_service.transfer(3, 999999999, 2147483649, 100)
        mock_print.assert_called_with(
            "Transaction number 3 was canceled due to non-existent origin account"
        )

    @patch("builtins.print")
    def test_transfer_non_existent_destination_account(self, mock_print):
        self.transfer_service.transfer(4, 938485762, 999999999, 100)
        mock_print.assert_called_with(
            "Transaction number 4 was canceled due to non-existent destination account"
        )


if __name__ == "__main__":
    unittest.main()
