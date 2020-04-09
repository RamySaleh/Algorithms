import unittest


class wallet():
    def __init__(self):
        self.wallet = self.loadWalletFromFile('wallet.txt')
        self.wallet.sort(reverse=True)

    def loadWalletFromFile(self, path):
        f = open(path, 'r')
        x = f.readline()
        f.close()
        return eval(x)

    def getBalance(self):
        return sum(self.wallet)

    def spend(self, amount):
        balance = self.getBalance()
        if amount > balance:
            return -1
        idx = 0
        change = 0
        cur_balance = 0
        while amount > 0:
            if amount >= self.wallet[idx]:
                amount -= self.wallet[idx]
                self.wallet[idx] = 0
                change = self.wallet[idx]
            else:
                cur_balance += self.wallet[idx]
                # if the rest is not enough -> take the money from the current coin
                if balance - cur_balance < amount:
                    self.wallet[idx] -= amount
                    change = self.wallet[idx]
                    amount = 0
            idx += 1
        return change


class wallet_tests(unittest.TestCase):
    def test_loadWalletFromFile(self):
        self.assertEqual([1000, 200, 200, 100, 50, 10, 1], wallet().wallet)

    def test_getBalance(self):
        self.assertEqual(1561, wallet().getBalance())

    def test_spend200(self):
        myWallet = wallet()
        self.assertEqual(0, myWallet.spend(200))
        self.assertEqual(1361, myWallet.getBalance())

    def test_spend300(self):
        myWallet = wallet()
        self.assertEqual(0, myWallet.spend(300))
        self.assertEqual(1261, myWallet.getBalance())

    def test_spend400(self):
        myWallet = wallet()
        self.assertEqual(0, myWallet.spend(400))
        self.assertEqual(1161, myWallet.getBalance())

    def test_spend250(self):
        myWallet = wallet()
        self.assertEqual(0, myWallet.spend(250))
        self.assertEqual(1311, myWallet.getBalance())

    def test_spend950(self):
        myWallet = wallet()
        self.assertEqual(50, myWallet.spend(950))
        self.assertEqual(611, myWallet.getBalance())