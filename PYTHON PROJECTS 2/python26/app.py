from PYTHON26 import employee

employee1 = employee("saad", 12, "python", True, 5, 25000)
employee2 = employee("nassim", 78, "C", False, 3.5, 7500)

print(employee1.salary)
employee1.bonus()
print(employee2.salary)
employee2.bonus()
