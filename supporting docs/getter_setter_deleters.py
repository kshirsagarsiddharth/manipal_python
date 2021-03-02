#%%
class Employee:
    def __init__(self,first: str,last: str) -> None:
        self.first = first 
        self.last = last 
        #self.email = first + '.' + last + '@email.com'

    # if we declare the decorator property on top of the 
    # email method we can access the email method as the attribute 
    # of the class 
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self) -> str:
        return f"{self.first} {self.last}"
    
    @fullname.setter 
    # we are declaring the setter for the full name method
    # with this setter we can access the fullname as an attribute
    # and pass in the full name.
    def fullname(self,name:str) -> None:
        # this method splits the name in the spaces
        first, last = name.split(' ')
        self.first = first 
        self.last = last 
    
    @fullname.deleter 
    def fullname(self):
        print('Delete Name!')
        self.first = None 
        self.last = None 
    

emp_1 = Employee('John','Smith')
emp_1.first = 'Siddharth'

print(emp_1.email)
print(emp_1.fullname)
emp_1.fullname = 'Rudra Singh'
# we want the email to be updated automatically when the first or last name 
# will be changed
# %%
# we want to access the employees full name metod as an attribute 
# and to that full name we want to pass an attribute 
# and by passing this attribute we also want to set the first and 
# last name of the employee 


