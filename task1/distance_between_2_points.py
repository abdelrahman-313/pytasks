from math import pow

def get_distance(point1,point2):
    # point1 (x1,y1)
    # point2 (x2,y2)

    return pow (pow(point2[0] - point1[0],2) +  pow(point2[1] - point1[1],2),0.5)


if __name__ == '__main__':
    print(get_distance((1,1),(1,2)))
