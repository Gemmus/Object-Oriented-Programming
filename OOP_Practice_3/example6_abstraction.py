# Abstraction:
# - natural extension of encapsulation
# - each object should only expose a higher level mechanism for using it
# - should hide internal implementation details
# - should only reveal the operations relevant to the other objects

class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # _ --> "protected" attribute (one underscore)
        # __ --> "private" attribute (double underscore)
        # both _ and __ are internal attributes
        self._salary = None
        self._num_bugs_solved = 0

    def code(self):
        self._num_bugs_solved += 1

    ##############
    #   Getter   #
    ##############
    def get_salary(self):
        return self._salary

    ##############
    #   Setter   #
    ##############
    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)

    #########################
    #   Internal function   #
    #########################
    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3


se = SoftwareEngineer("Max", 25)
for i in range(17):
    se.code()
# print(se._num_bugs_solved)
se.set_salary(6000)
print(se.get_salary())

