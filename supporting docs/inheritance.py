#%%
class Employee:
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.email = first+'.'+last+'@gmail.com'
        self.pay = pay 
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10 
    # we want our developer to have a programming language attribute 
    def __init__(self, first, last, pay, prog_lang):
        # we want the employee to handle the first name 
        # last name and pay
        super().__init__(first,last,pay)
        # in this case the super statement taking the 
        # attributes from Developer
        self.prog_lang = prog_lang 

class Manager(Employee):
    # passing list of employees this manager supervises 
    def __init__(self, first, last, pay, employees = None):
        # Inheriting from the Employee 
        super().__init__(first,last,pay)
        if employees is None: 
            self.employees = []
        else:
            self.employees = employees 
    
    def add_employee(self, emp):
        """
        This function takes an employee object
        and checks if it is present in the employees 
        list if not present it adds an employee to the 
        list
        """
        if emp not in self.employees: 
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        for emp in self.employees:
            print("-->",emp.fullname())

dev_1 = Developer('corey','schafer',50000,'python')
dev_2 = Developer('Test','Employee',60000,'Java')
mgr_1 = Manager('sue','allan',90000)

# %%
mgr_1.add_employee(dev_1)
# %%
mgr_1.add_employee(dev_2)
# %%
mgr_1.print_employees()
# %%
isinstance(mgr_1,Manager)
# %%
isinstance(mgr_1,Employee)
# %%
isinstance(mgr_1,Developer)
# %%
