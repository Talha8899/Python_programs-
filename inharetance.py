# applying oop concept
class Employee:

    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
        
        #function for showing details of emplyee
    def showdetais(self):
        print("role is:",self.role)
        print("department is:",self.department)
        print("salaray is:",self.salary)

#class enginer inherit the class employee and all its properties
class Engineer(Employee):

    #function for engineer name and age 
    def __init__(self,name,age):
        self.name=name
        self.age=age

        # inherit the init function of parent class 
        super().__init__("engr","it",80000)

#crating objects and passing parameter to construtor
s1=Employee("engineer","software engineering",80000)
s2=Engineer("abc",33)
print("name is:",s2.name)
s2.showdetais()