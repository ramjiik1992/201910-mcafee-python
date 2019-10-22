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
    #t1=Triangle.create(3,4,5)
    t1=None # change this
    t1.create(3,4,5) #make create object method
    test_shape(t1)

    #t2=Triangle.create(3,4,12)
    t2=None #change this
    t2.create(3,4,5) # make create object method
    test_shape(t2)

    c=Circle.create(7)
    test_shape(c)

    c2=Circle.create(-3)
    test_shape(c2)

main()




