class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):#__int__() -->constructor
        #Note: self in Python is equivalent to this in C++ or Java.
        #self.instance = argument
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves



harry = Employee("Harry", 255, "Instructor")

Employee.change_leaves(34)
print(harry.no_of_leaves)
print(harry.printdetails())
