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


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

print(Item.pay_rate)
print(item1.pay_rate)

print(Item.__dict__)  # All the attributes for Class level
print(item1.__dict__)  # All the attributes for instance level
