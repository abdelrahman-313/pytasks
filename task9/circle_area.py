from math import pi
def circle_area(rad):
    area = pi * (rad**2)
    print("The Area of the circle = %0.2f" % (area))

def circle_circumference(rad):
    circ = 2 * pi * rad
    print("The Circumference of the circle  = %0.2f" %(circ))
if __name__ == '__main__':

    radius = float(input("Please enter radius: "))
    circle_area(radius)
    circle_circumference(radius)