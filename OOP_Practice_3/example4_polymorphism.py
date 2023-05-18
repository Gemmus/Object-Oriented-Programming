class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")


class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def work(self):
        print(f"{self.name} is coding...")

    def debug(self):
        print(f"{self.name} is debugging...")


class Designer(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

    def work(self):
        print(f"{self.name} is designing...")

    def draw(self):
        print(f"{self.name} is drawing...")


####################
#   Polymorphism   #
####################

employees = [SoftwareEngineer("Paul", 35, 9000, "Senior"),
             SoftwareEngineer("Lisa", 25, 7000, "Junior"),
             Designer("Philip", 25, 5000),
             Employee("Daniel", 30, 4000)]


def motivate_employees(workers):
    for w in workers:
        w.work()


motivate_employees(employees)
