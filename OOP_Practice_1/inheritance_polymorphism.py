class User:
    def log(self):
        print(self)


class Teacher(User):
    def log(self):
        print("I'm a teacher")


class Customer(User):
    def log(self):
        print("I'm a customer")

    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    @property
    def name(self):
        # print("getting name")
        return self._name

    @name.setter
    def name(self, name):
        # print("setting name")
        self._name = name

    @name.deleter
    def name(self):
        # print("delete name")
        del self._name

    def update_membership(self, new_membership):
        self.membership_type = new_membership

    def __str__(self):
        # print("Converting to string")
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


# customer = [Customer("Caleb", "Gold"),
#             Customer("Alisa", "Silver"),
#             Customer("Donna", "Bronze"),
#             Teacher()
#             ]

# customer[0].log()
# customer[3].log()

users = [Customer("Caleb", "Gold"),
         Customer("Alisa", "Silver"),
         Customer("Donna", "Bronze"),
         Teacher()
         ]

for user in users:
    user.log()