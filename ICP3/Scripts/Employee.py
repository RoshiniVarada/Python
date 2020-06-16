class Employee:
    employeeCnt = 0
    totalsal = 0
    average = 0

    def __init__(self, name, surname,salary, department):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.department = department
        Employee.averageSal(salary)

    def averageSal(salary):
        Employee.employeeCnt += 1
        Employee.totalsal += salary
        Employee.average = Employee.totalsal / Employee.employeeCnt


class permanentEmployee(Employee):
    def __init__(self, name, surname, salary, department):
        Employee.__init__(self, name, surname, salary, department)


emp = Employee("Roshini1", "Varada1", 100000, "CS")
emp = Employee("Varada","Roshini", 1000056, "IT")
permanent = permanentEmployee("Roshini","Varada",2200400,"ECE")
emp = Employee("Roshini3","Varada3", 1000056, "IT")
print("Name of the permanent Employee",permanent.name)
print("Average Salary of the employee:",Employee.average)
print("Total Employee COunt:",Employee.employeeCnt)
