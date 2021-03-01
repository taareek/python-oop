#Class variable

class Employee():
    salary_raise = 1.07
    num_of_empls =0
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

        Employee.num_of_empls += 1

    def employee_information(self):
        print('Name: '+self.first_name+ ' '+ self.last_name)
        print('Salary: ' + str(self.salary))

    def apply_salary_raise(self):
        self.salary = self.salary * self.salary_raise
        return self.salary
        
         


rahim = Employee('Abdur','Rahim', 35000)
alex = Employee('Alex', 'Zingals', 25000)
print(type(rahim.salary))
rahim.employee_information()
print(rahim.apply_salary_raise())
alex.employee_information()
print(alex.apply_salary_raise())
print(rahim.__dict__)
print(alex.__dict__)
#print(Employee.__dict__)
rahim.salary_raise = 1.09         #updated salary for rahim
print(rahim.apply_salary_raise())
print(alex.apply_salary_raise())
print(rahim.__dict__)

print(Employee.salary_raise )   
print(alex.__dict__)  
print(rahim.salary_raise)
print(alex.salary_raise) # did not updated alex salary_raise as well as the class variable

print(Employee.num_of_empls)
faruk = Employee('Omar', 'Faruk', 75000)
print(faruk.employee_information())
print(Employee.num_of_empls)
