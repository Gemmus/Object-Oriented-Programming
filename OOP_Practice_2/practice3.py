class Item:
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

print(f'Total value of {item1.name} : {item1.calculate_total_price()}')
print(f'Total value of {item2.name}: {item2.calculate_total_price()}')

item2.has_numpad = False   # can be added more attributes, that is not all true to the whole class
