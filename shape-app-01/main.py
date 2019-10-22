from shapes.triangle import Triangle
from shapes.circle import Circle

def test_shape(shape):
    if not shape.is_valid():
        print('invalid ', type(shape).__name__)
    else:
        shape.draw('wall')
        print('perimeter',shape.perimeter())

    print()

def main():
    t1=Triangle() 
    t1.create(3,4,5) # can call using object reference
    test_shape(t1)

    t2=Triangle() #change this
    Triangle.create(t2,3,4,12) # can also call using class reference
    test_shape(t2)

    c=Circle.create(7) # can be called only using class refernce
    test_shape(c)

    c2=Circle.create(-3)
    test_shape(c2)

main()




