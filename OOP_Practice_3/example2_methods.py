class SoftwareEngineer:

    # class attribute
    alias = "Keyboard Magician"

    def __init__(self, position, name, age, level, salary=0):
        self.position = position
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f"{self.name} is coding...")

    def coding_language(self, language):
        print(f"{self.name} is coding in {language}")

    def __str__(self):
        return f"name = {self.name}, age = {self.age}, level = {self.level}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


se1 = SoftwareEngineer("Software Engineer", "Max", 20, "Junior", 5000)
print(se1.name)
print(se1.alias)
print(SoftwareEngineer.alias)

se2 = SoftwareEngineer("Software Engineer", "Lisa", 25, "Senior", 7000)
print(se2.name)

se1.code()
se2.code()

se1.coding_language("python")
se2.coding_language("C++")

print(se1)
print(se2)

se3 = SoftwareEngineer("Software Engineer", "Lisa", 25, "Senior", 7000)
print(se2 == se3)

print(se1.entry_salary(24))
print(SoftwareEngineer.entry_salary(27))
