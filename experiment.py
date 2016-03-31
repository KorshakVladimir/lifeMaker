class A(object):
    def get(self):
        self.x += 'a'

class B(object):
    def get(self):
        self.x += 'b'

class C(A):
    x = []
    def get(self):
        self.x += 'c'
        # super(A,self).get()
        A.get()

def x(z):
    z.data = 1

z = A() 
x(z)

print(z.data)        