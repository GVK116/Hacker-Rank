import math
class Points(object):
    def __init__(self, x, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        x1 = self.x - no.x
        y1 = self.y - no.y
        z1 = self.z - no.z
        r = Points(x1,y1,z1)
        return r

    def __truediv__(self, no):
        x1 = self.x
        y1 = no.x
        return x1/y1

    def dot(self, no):
        x1,y1,z1 = self.x * no.x , self.y * no.y , self.z * no.z
        return x1+y1+z1

    def cross(self, no):
        x1 = self.y*no.z - self.z * no.y
        y1 = -(self.x * no.z - self.z * no.x)
        z1 = self.x * no.y - self.y * no.x
        return Points(x1,y1,z1)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    # points =  [[0.0,4.0,5.0],[1.0,7.0,6.0],[0.0,5.0,9.0],[1.0,7.0,2.0]]

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)

    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
    print("%.2f" % math.degrees(angle))
