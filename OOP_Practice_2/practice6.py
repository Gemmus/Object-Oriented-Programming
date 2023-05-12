class Item:
    pay_rate = 0.8  # Discount 20%

    def __init__(self, name: str, price: float, quantity=0):  # with quantity set to 0, the type automatically becomes integer
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

print(f'Price of {item1.name}: {item1.price}')
item1.apply_discount()
print(f'Price of {item1.name}: {int(item1.price)}')

print(f'Price of {item2.name}: {item2.price}')
item2.pay_rate = 0.7
item2.apply_discount()
print(f'Price of {item2.name}: {int(item2.price)}')
