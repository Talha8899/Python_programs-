
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        value=0
        for i in self.marks:
            value+=i
        print(self.name,"your average number is",value/len(self.marks))
    
s1=Student("Talha",[23,35])
s1.get_avg()