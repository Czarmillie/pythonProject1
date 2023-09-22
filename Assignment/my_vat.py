def value_added_tax():
    while True:
        try:
            price = float(input("Enter the price of the item: "))
            vat_percent = float(input("Enter the VAT percentage: "))

            if price < 0 or vat_percent < 0:
                print("Both price and VAT must be positive numbers.")
            else:
                vat_price = price + (price * vat_percent / 100)
                return vat_price
        except (ValueError, SyntaxError, TypeError, KeyboardInterrupt, NameError, ZeroDivisionError):
            print("Invalid input. Please enter valid numbers.")

V_I_P = value_added_tax()
print("VAT including price:", V_I_P)