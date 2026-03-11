import matplotlib.pyplot as plt
import numpy as m
from Vector import Vector as V

def unpack(P):
    X = [i.x for i in P]
    Y = [i.y for i in P]
    Z = [i.z for i in P]
    return X, Y, Z

class Particle:

    def __init__(self,P,Q,R):
        self.P=P
        self.Q=Q
        self.R=R

    def initials(self,density=10,orientation=m.array([[1,0,0],[0,1,0],[0,0,1]])):
        points = []
        gr = (5**0.5 + 1)/2
        N=int(m.ceil(abs(self.Q)*density))
        for i in range(N):
            z = 1 - (i / (N-0.75-0.25*(-1)**N)) * 2
            radius = m.sqrt(1 - z * z)

            theta = 2*m.pi*gr * i

            x = m.cos(theta) * radius
            y = m.sin(theta) * radius

            points.append(V(x, y, z))

        points=[self.R*((orientation/abs(m.linalg.det(orientation))**(1/3))@i)+self.P for i in points]

        return points

    def plot(self,ax,col):
        r=self.R
        u = m.linspace(0, 2 * m.pi, 100)
        v = m.linspace(0, m.pi, 100)

        u, v = m.meshgrid(u, v)

        x = self.P.x+r * m.cos(u) * m.sin(v)
        y = self.P.y+r * m.sin(u) * m.sin(v)
        z = self.P.z+r * m.cos(v)

        ax.plot_surface(x, y, z, color=col)
        p=self.initials(density=5)
        ax.set_aspect('equal')








class Field:

    dx=1
    def __init__(self,F,V,particles,range,e):
        global dx
        self.F=F
        self.V=V
        self.end=particles
        dx=e
        self.r=range


    def nearEnd(self,P):
        return any(list(map(lambda x: abs(x.P-P)<0.9*x.R,self.end)))

    def inRange(self,P):
        return all([self.r[i][0]<P.V[i]<self.r[i][1] for i in range(3)])


    def line(self,P,reverse=False):
        L,c=[],[]
        while not self.nearEnd(P) and self.inRange(P):
            L.append(P)
            c.append(self.V(P))
            P+=(-1 if reverse else 1)*dx*self.F(P).unit()

        return L,c



