# Electric-Field
This project can be used to plot electric fields (and also magnetic fields).

Files to be used:
1) 01_System.py: Can be used to place charged particles in space and visualize the electric field.
2) 02_Earth.py: Rough modelling of Earth's magnetic field (Electric charge used instead of magnetic poles)

Steps to use 01_System.py:
1) Define the particles by specifying them in the array 'P', with their position vector, charge and radius.
2) Specify the range of display along x,y and z axes.
3) Specify the resolution, density of electric field lines w.r.t. charge and the contrast.
4) Call the 'run' function passing all the parameters.

Example Usage:
  P=[Particle(V(0,0,0),1,1)] 
  R=[[-10,10],[-10,10],[-10,10]]
  dx=0.5
  density=25
  run(P,R,dx,density)

Other Files:
1) Vector.py: Defines vector and all its  mathematical operations
2) Utiility.py: Defines particle, field and their properties relevant to the program.
