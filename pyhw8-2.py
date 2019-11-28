"""docstring for Person.• Create a class called Person.
In the class, define variables for storing date of
birth, place of birth, and male/female attributes.
In the class, define the constructor method, as well
as methods for returning current values of the class attributes."""
class Person(object):
    def __init__(self,DOB,POB,gender):
        super(Person, self).__init__()
        self.DOB = DOB
        self.POB = POB
        self.gender = gender
    def get_DOB(self):
        return self.DOB
    def get_POB(self):
        return self.POB
    def get_gender(self):
        return self.gender

"""Create a class called Employee.In the class,
define variables for storing date of hire, department,
and job title.  In the class, define the constructor method,
as well as methods for returning current values of the class
attributes."""
class Employee(Person):
    def __init__(self,DOB,POB,gender,DofHire,department,title):
        super(Employee, self).__init__(DOB,POB,gender)
        self.DofHire = DofHire
        self.department = department
        self.title = title

    def get_DofHire(self):
        return self.DofHire
    def get_department(self):
        return self.department
    def get_title(self):
        return self.title
    def set_DofHire(self):
        self.DofHire = DofHire
    def set_department(self):
        self.department = department
    def set_title(self):
        self.title = title


'''Create a class called Salaried that inherits
 from both Person and Employee classes.  In the class define variables
 for storing the salary and tax bracket.  In the class,
 define the constructor method, as well as methods for returning current
 values of the class attributes.'''
class Salaried(Employee,Person):
    def __init__(self, DOB,POB,gender,DofHire,department,title,salary,taxBracket):
        super(Salaried, self).__init__(DOB,POB,gender,DofHire,department,title)
        self.salary = salary
        self.taxBracket = taxBracket

    def get_salary(self):
        return self.salary
    def get_taxBracket(self):
        return self.taxBracket
    def set_salary(self):
        self.salary = salary
    def set_taxBracket(self):
        self.taxBracket = taxBracket

'''
Instantiate a Salaried object using the following attribute default
values: Date of birth: January 1, 1980; Place of birth: New York,
NY; Male, Date of hire: May 1, 2005, Department: Finance; Job Title:
Manager; Salary: 100000; Tax Bracket: 29%.
'''

newPerson = Salaried("January 1, 1980 ","New York, NY","Male","May 1, 2005","Finance","Manager",100000,.29)


print("Date of Birth  --> " + str(newPerson.DOB))
print("Place of Birth --> " + str(newPerson.POB))
print("Gender         --> "   + str(newPerson.gender))
print("Date of Hire   --> " + str(newPerson.DofHire))
print("department     --> " + str(newPerson.department))
print("title          --> "   + str(newPerson.title))
print("Salary         --> " + str(newPerson.salary))
print("Tax Bracket    --> " + str(newPerson.taxBracket))
