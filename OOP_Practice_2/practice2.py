class Item:
    def calculate_total_price(self, x, y):
        return x * y


item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
total1 = item1.calculate_total_price(item1.price, item1.quantity)
print(f'Phone: {item1.price} * {item1.quantity} = {total1}')

item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
total2 = item1.calculate_total_price(item2.price, item2.quantity)
print(f'Laptop: {item2.price} * {item2.quantity} = {total2}')
