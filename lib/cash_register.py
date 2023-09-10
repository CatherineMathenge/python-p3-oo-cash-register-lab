class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            self.total *= (100 - self.discount) / 100
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
     if self.items:
        last_item = self.items.pop()
        # Retrieve the price of the last item by its index in the list
        last_item_price = self.total - self.prices.pop()
        self.total -= last_item_price

# The following block is used for testing the code locally
if __name__ == "__main__":
    cash_register = CashRegister()
    cash_register_with_discount = CashRegister(20)

    cash_register.add_item("eggs", 0.98)
    cash_register.add_item("book", 5.00, 3)
    cash_register.add_item("Lucky Charms", 4.5)
    cash_register.add_item("Ritz Crackers", 5.0)
    cash_register.add_item("Justin's Peanut Butter Cups", 2.50, 2)

    cash_register_with_discount.add_item("macbook air", 1000)

    cash_register.apply_discount()
    cash_register_with_discount.apply_discount()

    cash_register.void_last_transaction()
    cash_register_with_discount.void_last_transaction()

    print(cash_register.total)  # Output should match the final total
    print(cash_register_with_discount.total)  # Output should match the final total
