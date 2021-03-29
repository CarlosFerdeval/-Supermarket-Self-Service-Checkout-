

from CheckoutRegister import CheckoutRegister
from Product import Product
from time import gmtime, strftime

current_date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
wishlist = []


def scan_product():
    '''Function to scan the product through the the item id from the scan_item function with the input bar code'''
    bar_code = input("\nScan Barcode: ")
    reg = CheckoutRegister(current_date_time, wishlist)
    product_details = reg.scan_item(bar_code)
    if product_details == None:
        print("This product does not exist in our inventory.\n")
        scan_another()
    else:
        print(product_details)
        wishlist.append(product_details)
        scan_another()


def scan_another():
    '''Function to past to scan_product in order to scan other product depending on the answer Y/N'''
    scan_another = input("Would you like to scan another product? (Y/N).")
    if scan_another == 'y' or scan_another == 'Y':
        scan_product()


def main():
    scan_product()
    reg = CheckoutRegister(current_date_time, wishlist)
    total_payment = reg.calculate_payment_due()
    change = reg.pay_money(total_payment)
    print("Change: $", change)
    reg.print_receipt()
    print("\nThank you for shopping at Carlos Shop!")
    # transactions = reg.save_transaction()
    reg.save_transaction()
    next = input("(N)ext customer, oPr (Q)uit? ")

    if next == "n" or next == "N":
        wishlist[:] = []
        main()
    else:
        # sys.exit(0)
        # transactions
        exit()


print("\n--------Welcome to Carlos Shop checkout!--------\n")

main()




