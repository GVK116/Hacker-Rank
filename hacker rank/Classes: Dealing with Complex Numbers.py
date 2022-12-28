import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real1 = self.real + no.real
        imag1 = self.imaginary + no.imaginary
        s3 = Complex(real1,imag1)
        return s3

    def __sub__(self, no):
        real1 = self.real - no.real
        imag1 = self.imaginary - no.imaginary
        s3 = Complex(real1,imag1)
        return s3

    def __mul__(self, no):
        real1 = self.real * no.real - self.imaginary * no.imaginary
        imag1 = self.imaginary * no.real + self.real * no.imaginary
        s3 = Complex(real1,imag1)
        return s3

    def __truediv__(self, no):
        real1 = (self.real * no.real + self.imaginary * no.imaginary)/(pow(no.real,2)+pow(no.imaginary,2))
        imag1 = (self.imaginary * no.real - self.real * no.imaginary)/(pow(no.real,2)+pow(no.imaginary,2))
        s3 = Complex(real1, imag1)
        return s3

    def mod(self):
        real1 = math.hypot(self.real,self.imaginary)
        imag1 = 0
        s3 = Complex(real1,imag1)
        return s3

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    comp1 = Complex(2,1)
    comp2 = Complex(5,6)
    print(comp1+comp2,comp1-comp2,comp1*comp2,comp1/comp2,Complex.mod(comp1),Complex.mod(comp2),sep="\n")


