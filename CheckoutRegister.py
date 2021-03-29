from time import strftime, gmtime

from Product import Product

current_date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
wishlist = []


class CheckoutRegister:

    def __init__(self, checkout_date, checkout_items):
        '''Constructor to set checkout_date to checkout_date, checkout_item to checkout_item, products to array[],
         file_name to product.txt, total to 0 and file_transactions to saletransaction.txt'''
        self.checkout_date = checkout_date
        self.checkout_items = checkout_items
        self.products = []
        self.file_name = 'product.txt'
        self.total = 0
        self.init()
        self.file_transactions = 'saleTransaction.txt'


    def init(self):
        '''Function to open and read the product.txt file'''
        # open product file for reading
        file = open(self.file_name, 'r')

        for line in file:
            line = line.split(',')
            product = Product(id=line[0], name=line[1], desc=line[2], price=str.rstrip(line[3]))
            self.products.append(product)
        file.close()

    def display_products(self):
        '''Function to deposit to display the products from Product'''
        for p in self.products:
            print(p)

    def add_item_to_cart(self, p):
        '''Function to add items to the list'''
        self.checkout_items.append(p)

    def display_checkout_items(self):
        '''Function to checkout the items from the list'''
        print("Checkout Items")
        print(self.checkout_items)

    def scan_item(self, product_id):
        '''Function to scan the item with the item id '''
        for p in self.products:
            if p.id == product_id:
                self.total = self.total + float(p.price)
                return p

    def calculate_payment_due(self):
        '''Funcion to calculate the final payment. Raises an
           exception if it receives a value that cannot be cast to float.'''

        try:
            cart_items = self.products
            cart_totals = 0
            for index, product in enumerate(self.checkout_items):
                cart_totals += float(product.price)
            self.due = cart_totals
            return cart_totals
        except ValueError:
         raise Exception('Please enter a valid floating point value.')

    def pay_money(self, total):
        '''Function to ask the user to pay the amount.  '''
        amount_to_pay = total
        print("\nPayment due: $" + str(amount_to_pay))
        change = self.accept_payment(amount_to_pay)
        return change

    def accept_payment(self, amount_to_pay):
            '''Function to accept the payment amount from the user. Raises an exception if it receives a value
            that cannot be cast to float. Raises an exception if it receives a  negative value'''

            # print("accept payment")
            paid = float(0.0)
            customer_pay = float(0.0)
            due = float(0.0)
            total = amount_to_pay
            due = True

            while due == True:
                try:
                    paid = float(input("\nPlease enter an amount to pay: "))
                    if paid < 0.0:
                        print("We don't accept negative money!\n")
                        continue
                    else:
                        customer_pay += paid
                        self.customer_pay = customer_pay
                        if paid < total:
                            due = total - paid
                            total = due
                            print("Payment due: $" + str(due))
                            due = True
                            continue
                        else:
                            change = paid - total
                            self.change = change
                            # print("Change: ",change)
                            return change
                        break
                    break

                except ValueError:
                    print('Please enter a  float value.')

    def print_receipt(self):
        ''''Function to Print the final receipt with the total amount, amount received and change given'''
        print("\n----- Final Receipt -----\n")

        print(str(self.checkout_items))

        print("\n")
        print("Total amount due:", '      $' + str(self.due))
        print("Amount Received:", '       $' + str(self.customer_pay))
        print("Change Given:", '          $' + str(self.change), '\n')

    def save_transaction(self):
        ''''Function to save the transaction amount and the date and time to a saleTransaction.txt file '''
        transactions = open(self.file_transactions, "a")
        print("Transaction amount:", '  $' + str(self.due), '\n'"Date and Time:", current_date_time, '\n',
              file=transactions)

        transactions.close()


