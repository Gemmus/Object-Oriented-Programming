class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        print("customer created")


customer = [Customer("Caleb", "Gold"),
            Customer("Alisa", "Silver")]

c = customer[0]
print(c.name, c.membership_type)
# or
print(customer[0].name, customer[0].membership_type)

d = customer[1]
print(d.name, d.membership_type)
