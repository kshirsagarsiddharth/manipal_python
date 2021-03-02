#%%
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    def __repr__(self) -> str:
        # returning the string to re create the object
        return f"Employee('{self.first}' '{self.last}' '{self.pay}')"
    
    def __str__(self) -> str:
        # this returns object.fullname and object.email 
        # i.e when we iniatialize the object and when we print the 
        # object this method is called this method returns the 
        # full name and the email.
        return f"{self.fullname()} - {self.email}"
    
    def __add__(self: object ,other: object) -> int:
        """
        self: left side of addition
        other: right side of addition
        """
        return self.pay + other.pay 
    
    def __len__(self: object) -> int:
        # when the __len__ function is called on the object 
        # this method is invoked and it returns the length 
        # of full name of the employee
        return len(self.fullname())

emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Siddharth','Kshirsagar',600000)

emp_1 + emp_2
# %%
# add two employees objects togther and the result of the addition should
# be sum of their salaries 

len(emp_1)
# %%
