import unittest


from CheckoutRegister import CheckoutRegister

wishlist = []


class TestCheckoutRegister(unittest.TestCase):
    # def test_accept_payment(self):
    #     self.assertEqual(True, False)

    def test_can_instantiate_class(self):
        checkout = CheckoutRegister(2020, 1)

    def setUp(self):
        # setup instance of class for tests that follow
        self.checkout = CheckoutRegister(2020, 1)

    def test_list(self):
        # check the products in the array list
        self.checkout.products = ['milk', "bread", "sugar"]

    def test_scan_item(self):
        # test the scan product with the id
        p100 = self.checkout.products
        self.assertEqual(self.checkout.products, p100)

    def test_display_checkout_items(self):
        # test to be sure that the items selected are in the checkout_items
        my_items = ['bread', 'sugar']
        item = 'sugar'
        self.assertIn(item, my_items)
        self.checkout.display_checkout_items()

    def test_calculate_payment_due(self):
        # illegal amount (like 'bananas'
        # or such - something which is NOT a float) raises a suitable exception
        self.assertRaises(Exception, self.checkout.calculate_payment_due, 'bananas')

    def test_accept_payment_illegal_value(self):
        # something which is NOT a float) results in an exception being raised
        self.assertRaises(Exception, self.checkout.accept_payment)


if __name__ == '__main__':
    unittest.main()
