import numpy as np
from math import sin, cos, log
from Phugoid_Oscillation import Euler_Step
import matplotlib.pyplot as plt

#This is a test to try and optimize for the case of projectile motion


#Some initial conditions
g = 9.81
v0 = 100.
theta = np.linspace(0.0, np.pi/2,10000)
y0 = 0.
x0 = 0.0

#Define time of flight and step size
dt = 0.01

#Here is the function used in the Euler_Step

def f_proj (u):
    vy = u[0]
    th = u[1]
    y = u[2]
    x = u[3]
    
    
    return np.array([-g,0.0,vy, v0*cos(th)])

optimal = [-1,0,0]
for th in theta:
    u= np.array([v0*sin(th),th,y0,x0])
    u1 = u[:]
    while (u[2] >= 0):
        u1 = u[:]
        u = Euler_Step(u, f_proj, dt)
    if u[-1] > optimal[0]:
        optimal = [u[-1],th,u[2]]
               
        

print optimal
"""
plt.figure(figsize=(8,6))
plt.grid(True)
plt.xlabel(r'x',fontsize = 18)
plt.ylabel(r'y', fontsize = 18)
plt.title('Projectile Motion: Flight Time = %.2f'% T, fontsize =18)
plt.plot(x,y)

plt.show()
"""


