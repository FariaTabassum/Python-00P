
class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print("Instance Variable")
rohan.no_of_leaves = 9
print(rohan.no_of_leaves)
print(rohan.__dict__)
print("\n class Variable")
Employee.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)

print(harry.__dict__)
print(harry.no_of_leaves)


