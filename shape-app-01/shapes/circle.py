import math

class Circle:
    def create(radius):
        t=Circle()
        t.radius=radius
        t.valid=radius>0
        return t
        
    def is_valid(self):
        return  isinstance(self,Circle) and self.valid
                

    def perimeter(self):
        if self.is_valid() :
            return 2*math.pi*self.radius
        else:
            raise ValueError('invalid sides.')
            
    def draw(self,surface):
        if self.is_valid():
            print(f'Circle({self.radius}) drawn on {surface}')
        else:
            print('Invalid Circle')
