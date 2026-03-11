from matplotlib import colors
import numpy as np
from matplotlib.colors import ListedColormap
from scipy.stats import ortho_group
from Line import *
from Vector import Vector as V
from mpl_toolkits.mplot3d.art3d import Line3DCollection

def run(P,R,dx,density,ax=None,displaycharge=True,contrast=3):

    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

    Cmax = max([abs(i.Q / i.R) for i in P])
    top = plt.get_cmap('YlGnBu_r', 128)
    bottom = plt.get_cmap('YlOrRd', 128)
    newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                           bottom(np.linspace(0, 1, 128))))
    RB = ListedColormap(newcolors, name='RB')
    norm = colors.Normalize(vmin=-1, vmax=1)

    def col(c):
        return RB(norm(np.sign(c) * np.abs(c) ** (1/contrast)))

    Pstart, Nstart = [], []
    for i in P:
        if i.Q > 0:
            Pstart.extend(i.initials(density=density, orientation=ortho_group.rvs(dim=3)))
        else:
            Nstart.extend(i.initials(density=density, orientation=ortho_group.rvs(dim=3)))
        if displaycharge: i.plot(ax, col(i.Q / i.R / Cmax))

    def E(X):
        e = V(0, 0, 0)
        for i in P: e += i.Q * (X - i.P).unit() / abs(X - i.P) ** 2
        return e

    def pot(X):
        e = 0
        for i in P: e += i.Q / abs(X - i.P)
        return e

    F = Field(E, pot, P, R, dx)

    L, C = [], []
    for i in Pstart:
        l, c = F.line(i)
        L.append(l)
        C.append(c)

    for i in Nstart:
        l, c = F.line(i, reverse=True)
        L.append(l)
        C.append(c)

    for i in range(len(L)):
        X, Y, Z = unpack(L[i])
        C[i] = np.array(C[i]) / Cmax

        points = np.array([X, Y, Z]).T.reshape(-1, 1, 3)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)

        lc = Line3DCollection(segments, cmap=RB)
        lc.set_array(np.sign(C[i]) * np.abs(C[i]) ** (1/contrast))
        lc.set_clim(vmin=-1, vmax=1)
        lc.set_linewidth(1)

        ax.add_collection3d(lc)

    ax.set_aspect('equal')

    plt.show()


#Test
'''
P=[Particle(V(0,0,0),1,1)]
R=[[-10,10],[-10,10],[-10,10]]
dx=0.5
density=25
run(P,R,dx,density)
'''
