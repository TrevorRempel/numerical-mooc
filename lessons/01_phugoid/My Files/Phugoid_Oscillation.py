import numpy as np
from math import sin, cos, log, ceil
import matplotlib.pyplot as plt
from matplotlib import rcParams          #Allows us to set notebook wide plotting parameters

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

        
#Impliments a single step in the Euler method: u(t + dt) = u(t) + dt*u_prime(u(t))        
def Euler_Step (u, u_prime, dt):
    
    return u + dt*u_prime(u)
    
#Computes the difference between two solutions, one on the current grid and the other
#on a finer grid

def get_griddiff(u_current,u_fine,dt):
    space_current = len(u_current[:,0])
    space_fine = len(u_fine[:,0])
    
    grid_ratio = ceil(space_fine/float(space_current))
    
    diffgridx = dt*np.sum(np.abs(u_current[:,2] - u_fine[::grid_ratio,2]))
    diffgridy = dt*np.sum(np.abs(u_current[:,3] - u_fine[::grid_ratio,3]))
    
    return max(diffgridx,diffgridx)


#Define the parameters for the model
g = 9.81        #acceleration due to gravity
v_t = 60.      #trim velocity 
C_D = 1/40.     #Drag coefficeint --- or D/L if C_L = 1.0
C_L = 1         #For convenience we put C_L = 1  


#Initial Conditions
v0 = v_t        #Start at the trim velocity
theta0 = 0.0     #Initially horizonatl
x0 = 0.0         #Horizontal position -- arbitrary
y0 = 1000.0      #Initial altitude


#Define u_prime for this model
def f_phugoid(u):
    #u is a four array  u= (v,theta,x,y)
    
    v = u[0]
    theta = u[1]
    x = u[2]
    y=u[3]
    
    return np.array([-g*sin(theta) - C_D/C_L*g/v_t**2*v**2, -g/v*cos(theta)
                        +g/v_t**2*v, v*cos(theta), v*sin(theta)])
    


#Choose the flight time
T = 100.

#We would like to test this model for several values of the time step dt

#dt_values = np.array([0.1,0.05,0.01,0.005,0.001])
dt_values = np.array(range(0,6))*0.2*np.pi
dt = 0.01
#Will hold the solutions one for each value of dt
u_values = np.empty_like(dt_values, dtype = np.ndarray)

#Perform Eulers method for each dt

for i,vin in enumerate(dt_values):
   
    N = int(T/dt) + 1                        #Number of time steps
    
    #Initilize array to hold the soltuion and then put first element equal to the initial conditions
    u = np.empty((N,4))
    u[0] = np.array([v0,vin,x0,y0])
    
    #Run Eulers method
    for j in range (N-1):
        u[j+1] = Euler_Step(u[j],f_phugoid,dt)
    
    #Store solution is u_vales
    u_values[i] = u    
'''
#Make an array of grid differences
griddiff = np.empty_like(dt_values)

for i, dt in enumerate(dt_values):
    
    print ('dt = {}'.format(dt))
    #Find grid differences between a given grid and the finest one we computed
    
    griddiff[i] = get_griddiff(u_values[i],u_values[-1],dt)

'''
#We are now ready to plot the trajectories

plt.figure(figsize=(8,6))
plt.grid(True)
plt.xlabel(r'x',fontsize = 18)
plt.ylabel(r'y', fontsize = 18)
plt.title('Glider Trajectory: Flight Time = %.2f'% T, fontsize =18)

for i in range(len(dt_values)):
    plt.plot(u_values[i][:,2],u_values[i][:,3], lw = 2, label = '%.2f'%dt_values[i])
plt.legend()
'''
#Plot the grid differences on log-log scale
plt.figure(figsize = (6,6))
plt.grid(True)
plt.xlabel(r'$\Delta t$',fontsize = 18)
plt.ylabel(r'$L_1$--norm of grid difference', fontsize = 18)
plt.axis('equal')
plt.loglog(dt_values[:-1],griddiff[:-1],color ='r', ls = '-', lw=2,marker = 'o')

'''
plt.show()

    





























