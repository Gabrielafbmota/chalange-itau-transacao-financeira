import unittest
from entities.account import Account
from repositories.account_repository_memory import AccountRepositoryMemory


class TestAccountRepositoryMemory(unittest.TestCase):
    def setUp(self):
        self.repository = AccountRepositoryMemory()

    def test_get_account(self):
        account = self.repository.get_account(938485762)
        self.assertIsNotNone(account)
        self.assertEqual(account.number, 938485762)
        self.assertEqual(account.balance, 180)

    def test_update_account(self):
        account = self.repository.get_account(938485762)
        account.balance = 200
        self.repository.update_account(account)

        updated_account = self.repository.get_account(938485762)
        self.assertEqual(updated_account.balance, 200)

    def test_get_non_existent_account(self):
        account = self.repository.get_account(999999999)
        self.assertIsNone(account)


if __name__ == "__main__":
    unittest.main()
