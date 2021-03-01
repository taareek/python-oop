#Classes and instances
class Employee():
    def __init__(self, first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = first_name + last_name + str(age) + '@gmail.com'

    def show_employee_information(self):
        print('Name: '+self.first_name+' '+ self.last_name)
        print('Age: '+str(self.age))
        print('Email: '+self.email)

#emp_1 = Employee()
#emp_2 = Employee()
#print(emp_1)
#print(emp_2)
#emp_1.name = 'Tarek Aziz'
#print(emp_1.name)

emp_t = Employee('Tarek', 'Aziz', 24)
print(emp_t.first_name)
print(emp_t.email)
print("///////////////////////////////")
#print('{} {}'.format(emp_t.first_name, emp_t.last_name))
#print(emp_t.show_employee_information())         This will also work
emp_t.show_employee_information()