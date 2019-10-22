


class Triangle:
    def create(s1,s2,s3):
        t=Triangle()
        t.s1=s1
        t.s2=s2
        t.s3=s3
        t.validate()
        return t
        
    def validate(self):
        self.valid=self.s1>0 and self.s2>0 and self.s3>0 \
                and self.s1+self.s2>self.s3 \
                and self.s1+self.s3>self.s2 \
                and self.s2+self.s3>self.s1 
        

    def is_valid(self):
        return  isinstance(self,Triangle) and self.valid
                

    def perimeter(self):
        if self.is_valid() :
            return self.s1+self.s2+self.s3
        else:
            raise ValueError('invalid sides.')
            
    def draw(self,surface):
        if self.is_valid():
            print('Triangle<{},{},{}> drawn on {}'.format(self.s1,self.s2,self.s3,surface))
        else:
            print('Invalid Triangle')
