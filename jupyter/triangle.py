
def is_valid(s1,s2,s3):
    return s1>0 and s2>0 and s3>0 and s1+s2>s3 and s2+s3>s1 and s1+s3>s2

def perimeter(s1,s2,s3):
    if is_valid(s1,s2,s3):
        return s1+s2+s3
    else:
        return None
    
def draw(s1,s2,s3, canvas):
    if is_valid(s1,s2,s3):
        print(f'Triangle<{s1},{s2},{s3}> drawn on {canvas}')
    else:
        print('invalid triangle')
        
