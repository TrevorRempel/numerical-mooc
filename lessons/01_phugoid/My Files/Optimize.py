#We will use the Phugoid model to obtain the best launch angle and velocity for a paper airplane

import numpy as np
from math import sin, cos, log
from Phugoid_Oscillation import f_phugoid, Euler_Step
import matplotlib.pyplot as plt
from matplotlib import rcParams          #Allows us to set notebook wide plotting parameters

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16
  


#Define the parameters for the model
g = 9.81        #acceleration due to gravity
v_t = 4.9      #trim velocity 
C_D = 1/5.     #Drag coefficeint --- or D/L if C_L = 1.0
C_L = 1         #For convenience we put C_L = 1  

    
#Initial Conditions
x0 = 0.0         #Horizontal position choose to be origin so x is distance travelled
y0 = 10.0      #Initial altitude
v0 = np.linspace(1,101,100)*v_t
theta0 = np.array([0.0])


#Choose suitable value for dt
dt = 0.01

optimal = [-1,0,0]   #Will use list to hold values for [distance, v0,theta0]

for refine in range(3):
    print refine
    for v in v0:
        for theta in theta0:
            u = np.array([v,theta,x0,y0])
            while (u[-1] >= 0):
                    u = Euler_Step(u,f_phugoid,dt)
            if u[2] > optimal[0]:
                optimal = [u[2], v, theta]
                
    v0 = np.linspace(optimal[1] - v_t*100**(-refine),optimal[1] + v_t*100**(-refine),100)
     
        
print optimal         
