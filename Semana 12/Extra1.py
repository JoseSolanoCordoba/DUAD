class Employee:
    def __init__(self, name, salary):
        self._name = name
        self. _salary = salary
    
    @property
    def name (self):
        return f'{self._name}'
    
    @property
    def salary (self):
        return f'{self._salary}'
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("Salary must be greater than zero")

    def promote (self, percentage):
        self._salary = self._salary*(1+percentage)

employee1 = Employee("Jose", 500)
print("Employee name: " + employee1.name)
print("Employee salary: " + employee1.salary)
employee1.promote(0.15)
print("New employee salary with promotion: " + employee1.salary)
employee1.salary = 1000
print("New employee salary in new company: " + employee1.salary)
employee1.salary = -1000
employee1.salary = 0
