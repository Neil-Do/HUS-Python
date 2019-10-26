class Employee:

    def __init__(self, id, name, birthday, baseSalary):
        self.id = id
        self.name = name
        self.birthday = birthday
        self.baseSalary = baseSalary


class Manager(Employee):

        def __init__(self, id, name, birthday, baseSalary):
            super().__init__(id, name, birthday, baseSalary)

        def getSalary(self):
            return self.baseSalary * 1.25


class DataScientist(Employee):

    def __init__(self, id, name, birthday, baseSalary, monthyProject = 0):
        super().__init__(id, name, birthday, baseSalary)
        self.monthyProject = monthyProject

    def getSalary(self):
        return self.baseSalary * 1.20 + self.monthyProject * 1500


class Developer (Employee):

    def __init__(self, id, name, birthday, baseSalary, monthyProject = 0):
        super().__init__(id, name, birthday, baseSalary)
        self.monthyProject = monthyProject

    def getSalary(self):
        return self.baseSalary + self.monthyProject * 1000
