import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.x =real
        self.y =imaginary 
        # z = x + iy complex equantion
        
    def __add__(self, no):
        a = self.x+no[1]
        b = self.y+no[2]
        
    def __sub__(self, no):
        pass
        
    def __mul__(self, no):
        pass

    def __truediv__(self, no):
        pass

    def mod(self):pass

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
    print("Hi")