import numpy as np

class Vector:

    __array_ufunc__ = None

    def __init__(self,x,y,z):
        self.V=np.array([x,y,z])
        self.x,self.y,self.z=x,y,z

    def __add__(self, other):
        return Vector(*(self.V+other.V))

    def __sub__(self, other):
        return Vector(*(self.V - other.V))

    def dot(self, other):
        return np.sum(self.V*other.V)

    def cross(self, other):
        p=[0,0,0]
        for i in range(3):
            p[i]=self.V[(i+1)%3]*other.V[(i-1)%3]-self.V[(i-1)%3]*other.V[(i+1)%3]
        return Vector(*p)

    def __abs__(self):
        return np.sum(self.V**2)**0.5

    def unit(self):
        return self/abs(self)

    def __rmul__(self,scalar):
        return Vector(*(self.V*scalar))

    def __truediv__(self,scalar):
        return Vector(*(self.V/scalar))

    def __iadd__(self,other):
        self=self+other
        return self

    def __neg__(self):
        return (-1)*self

    def __rmatmul__(self, other):
        return Vector(*np.transpose(other@np.transpose(self.V)))

    def __str__(self):
        return f"({self.V[0]},{self.V[1]},{self.V[2]})"

    def __repr__(self):
        return f"({self.V[0]},{self.V[1]},{self.V[2]})"






#test
'''
v=Vector(1,1,1)
print(v)
u=Vector(0,0,1)
print(u+v)
print(-v)
print(abs(v))
print(u.dot(v))
print(u.cross(v))
print(np.array([[1,2,3],[2,3,4],[4,5,6]])@u)
'''