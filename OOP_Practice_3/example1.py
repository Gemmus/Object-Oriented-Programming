class SoftwareEngineer:

    # class attribute
    alias = "Keyboard Magician"

    def __init__(self, position, name, age, level, salary=0):
        self.position = position
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary


se1 = SoftwareEngineer("Software Engineer", "Max", 20, "Junior", 5000)
print(se1.name)
print(se1.alias)
print(SoftwareEngineer.alias)
se2 = SoftwareEngineer("Software Engineer", "Lisa", 25, "Senior", 7000)
print(se2.name)

