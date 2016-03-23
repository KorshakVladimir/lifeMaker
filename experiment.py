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

c_ins = C()
c_ins.get()
print(c_ins.x)        