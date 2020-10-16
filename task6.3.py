class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']

class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        total_income = self._income_wage + self._income_bonus
        print(total_income)


worker1 = Position('Anton', 'Borisoff', 'Direktor', {'wage': 10000, 'bonus': 50000})
worker1.get_full_name()
worker1.get_total_income()