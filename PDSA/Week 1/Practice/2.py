class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def is_valid(self):
        x=self.a
        y=self.b
        z=self.c
        if x+y>z and x+z>y and y+z>x:
            return "Valid"
        else:
            return "Invalid"
    def Side_Classification(self):
        if self.is_valid() =="Invalid":
            return "Invalid"
        else:
            if self.a==self.b==self.c:
                return 'Equilateral'
            elif (self.a==self.b) or (self.b==self.c) or (self.a==self.c):
                return 'Isosceles'
            else:
                return 'Scalene'
    def Angle_Classification(self):
        if self.is_valid() =="Invalid":
            return "Invalid"
        else:
            if (self.a)**2+(self.b)**2<(self.c)**2:
                return 'Obtuse'
            elif (self.a)**2+(self.b)**2==(self.c)**2: 
                return 'Right'
            elif (self.a)**2+(self.b)**2>(self.c)**2: 
                return 'Acute'
    def Area(self):
        if self.is_valid() =="Invalid":
            return "Invalid"
        else:
             s=(self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5  
                 
                      
                                 
                
            
                 
        
    
a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())