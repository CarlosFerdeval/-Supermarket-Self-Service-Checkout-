import unittest

from Product import Product


class TestProduct(unittest.TestCase):
    #
    def test_can_instantiate_class(self):
        product = Product('id', 'name', 'desc', 'price')

    def setUp(self):

        # setup instance of class for tests that follow
        # Create a test BankAccount object
        self.products = Product('id', 'name', 'desc', 'price')


if __name__ == '__main__':
    unittest.main()
