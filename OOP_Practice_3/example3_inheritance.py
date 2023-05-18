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


se = SoftwareEngineer("Paul", 35, 9000, "senior")
se.work()
se.debug()
d = Designer("Philip", 25, 5000)
d.work()
d.draw()
a = Employee("Daniel", 30, 4000)
a.work()
