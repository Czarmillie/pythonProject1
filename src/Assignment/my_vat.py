def your_vat():
    while True:
        try:
            price = float(input("Enter the price of the item: "))
            vat_percent = float(input("Enter the VAT percentage: "))

            if price < 0 or vat_percent < 0:
                print("Both price and VAT must be positive numbers.")
            else:
                vat_inclusive_price = price + (price * vat_percent / 100)
                return vat_inclusive_price
        except ValueError:
            print("Invalid input. Please enter valid numbers.")


vat_inclusive_price = your_vat()
print("VAT inclusive price:", vat_inclusive_price)