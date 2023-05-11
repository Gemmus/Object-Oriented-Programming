class Customer:
    def __init__(self, name, membership_type):  # def __init__ called initializer or constructor, parameters are passed
        self.name = name
        self.membership_type = membership_type

    def update_membership(self, new_membership):
        self.membership_type = new_membership

    def read_customer():
        print("Static method, not attached to any individual object, but invoke on the class itself")

    def __str__(self):
        print("Converting to string")
        return self.name + " " + self.membership_type

    def print_all(customers):
        for i in customers:
            print(i)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True

        return False

    __hash__ = None
    __repr__ = __str__


customer = [Customer("Caleb", "Gold"),
            Customer("Alisa", "Silver"),
            Customer("Donna", "Bronze"),
            Customer("Pete", "Platinum"),
            Customer("Zara", "Gold"),
            Customer("Brad", "Silver"),
            Customer("Joseph", "Bronze"),
            Customer("Kati", "Platinum"),
            Customer("Caleb", "Gold"),
            Customer("Kati", "Platinum")
            ]

print(customer[0].name, customer[0].membership_type)

customer[0].update_membership("Platinum")
print(customer[0].name, customer[0].membership_type)

Customer.read_customer()

print(customer[4])

Customer.print_all(customer)

print(customer[7] == customer[9])

print(customer)
