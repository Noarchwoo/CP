# Complex class and dummy test

class Complex:
    def __init__(z, x, y):
        z.re=x
        z.im=y

    def addt(z1, z2):
        return Complex(z1.re+z2.re, z1.im + z2.im)

    def subt(z1, z2):
        return Complex(z1.re-z2.re, z1.im - z2.im)

    def __repr__(self):
        return '%f, %f' %(self.re, self.im)


z1 = Complex(2, 2)
print 'z1 = ', Complex.addt(z1, z1)
