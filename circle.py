class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
       return (self.radius**2)*3.14
    
    def parameter(self):
        return 2*3.14*self.radius
    
s1=Circle(5)
print(s1.area(),s1.parameter())