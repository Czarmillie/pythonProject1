class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))


class CheckoutSystem:
    def __init__(self):
        self.products = {}
        self.cart = ShoppingCart()

    def add_product(self, name, price):
        self.products[name] = Product(name, price)

    def process_checkout(self, cashier_name, discount):
        total = 0
        for product, quantity in self.cart.items:
            total += product.price * quantity

        discount_amount = total * (discount / 100)
        vat = total * 0.075
        bill_total = total - discount_amount + vat

        print("SEMICOLON STORES")
        print("MAIN BRANCH")
        print("Location: 312, HERBERT MACAULY WAY, SABO YABA, LAGOS.")
        print("Tel: 03293828343")
        print("Date: 18-Dec-22 8:48:11 pm")
        print("Cashier:", cashier_name)
        customer_name = input("What is the customer’s name? ")
        print("==============================================")
        print("ITEM\t\tQTY\t\tPRICE\t\tTOTAL(NGN)")
        print("------------------------------------------------------------")

        for product, quantity in self.cart.items:
            print(f"{product.name}\t\t{quantity}\t\t{product.price:.2f}\t\t{product.price * quantity:.2f}")

        print("------------------------------------------------------------")
        print(f"Sub Total:\t\t\t{total:.2f}")
        print(f"Discount:\t\t\t{discount_amount:.2f}")
        print(f"VAT @ 17.5%:\t\t{vat:.2f}")
        print("==============================================")
        print(f"Bill Total:\t\t{bill_total:.2f}")

        amount_paid = float(input("How much did the customer give to you?\n"))
        balance = amount_paid - bill_total

        print("==============================================")
        print("SEMICOLON STORES")
        print("MAIN BRANCH")
        print("Location: 312, HERBERT MACAULY WAY, SABO YABA, LAGOS.")
        print("Tel: 03293828343")
        print("Date: 18-Dec-22 8:48:11 pm")
        print("Cashier:", cashier_name)
        print("Customer name:", customer_name)
        print("==============================================")
        print("ITEM\t\tQTY\t\tPRICE\t\tTOTAL(NGN)")

        for product, quantity in self.cart.items:
            print(f"{product.name}\t\t{quantity}\t\t{product.price:.2f}\t\t{product.price * quantity:.2f}")

        print("Sub Total: \t\t", total)
        print("Discount: \t\t", discount_amount)
        print("VAT @17.5%: \t\t", vat)
        print("==============================================")
        print("Bill Total: \t\t", bill_total)
        print("Amount Paid: \t\t", amount_paid)
        print("Balance: \t\t", balance)
        print("=================================================")
        print("THANK YOU FOR YOUR PATRONAGE")
        print("=================================================")

checkout = CheckoutSystem()

num_products = int(input("How many products do you want to add? "))
for i in range(num_products):
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    checkout.add_product(name, price)

while True:
    product_name = input("What did the user buy? ")
    quantity = int(input("How many pieces?"))
    if product_name in checkout.products:
        checkout.cart.add_item(checkout.products[product_name], quantity)
    else:
        print("Product not found. Please enter a valid product name.")
    more_items = input("Add more items? (yes/no) ")
    if more_items.lower() == "no":
        break

cashier_name = input("What is your name? ")
discount = float(input("How much discount will he get? "))
checkout.process_checkout(cashier_name, discount)