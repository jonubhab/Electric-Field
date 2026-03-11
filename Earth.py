from System import run
from Line import *
from Vector import Vector as V

P=[Particle(V(0,0,5),1.6,1),
   Particle(V(0,0,-5),-0.4,1),
   Particle(V(0,5,0),-0.4,1),
   Particle(V(0,-5,0),-0.4,1),
   Particle(V(0,3.5355339,3.5355339),-0.1,1),
   Particle(V(0,3.5355339,-3.5355339),-0.1,1),
   Particle(V(0,-3.5355339,-3.5355339),-0.1,1),
   Particle(V(0,-3.5355339,3.5355339),-0.1,1)]
R=[[-20,20],[-20,20],[-20,20]]
dx=0.5
density=100
displaycharge=False
contrast=3

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

earth=Particle(V(0,0,0),0,7)
earth.plot(ax,(1,1,0,1))

run(P,R,dx,density,ax,displaycharge,contrast)