"""

Course FM1220 Automatic Control at USN

Compulsory assignment 1:
Programming a simulator of an heated tank in Python

Solution to Problem 2:
"Programming and simulation: Program a simulator of the
tank heater in Python. The simulator must be implemented 
with "native" code in a For loop based on the Euler 
Forward discretization of the model (a built-in simulation 
function of Python should not be used). You can set the 
time-step to 1 s. The following variables should be plotted:
T, Tin, Tenv, and P with temperatures in one subplot,
and P in another subplot.
Run a simulation with P = P0 as calculated in Problem 1.
Is the simulated static T the same as specified in
Problem 1?

Finn Aakre Haugen
finn.haugen@usn.no

2021 09 01

"""

#%% Imports:

import numpy as np
import matplotlib.pyplot as plt

#%% Model params:

c = 4200 # [J/(kg*K)]
rho = 1000 # [kg/m3]
V = 0.2 # [m3]
U = 1000 # [W/K]
F = 0.25e-3  # [m3/s]
T_in = 20  # [deg C]
T_env = 20  # [deg C]

T_min = 0
T_max = 100

#%% Calculation of power giving specified static temp: 

T_static = 25  # [deg C]  Static temp

# From model after t' is set to zero (static value): 
P0 = - (c*rho*F*(T_in-T_static) + U*(T_env-T_static))  # [W]

#%% Sim time settings:

dt = 1  # [s]
t_start = 0  # [s]
t_stop = 6000  # [s]
N_sim = int((t_stop - t_start)/dt) + 1

#%% Preallocation of arrays for storing:

t_array = np.zeros(N_sim)
T_array = np.zeros(N_sim)
T_in_array = np.zeros(N_sim)
T_env_array = np.zeros(N_sim)
P_array = np.zeros(N_sim)

#%% Sim loop:

T_k = T_init = 20  # [deg C] Initial temp

for k in range(0, N_sim):

    t_k = k*dt
    
    P_k = P0
    T_in_k = T_in
    T_env_k = T_env
    
    dT_dt_k = ((1/(c*rho*V))
               *(P_k
                 + (c*rho*F)*(T_in-T_k) 
                 + U*(T_env-T_k)))
    T_kp1 = T_k + dt*dT_dt_k
    T_kp1 = np.clip(T_kp1, T_min, T_max)
    
    t_array[k] = t_k
    T_array[k] = T_k
    T_in_array[k] = T_in_k
    T_env_array[k] = T_env_k
    P_array[k] = P_k

    
    # Time index shift:
    T_k = T_kp1

# %% Plotting:

plt.close('all')
plt.figure(1)

plt.subplot(2, 1, 1)
plt.plot(t_array, T_array, 'r', label='T')
plt.plot(t_array, T_in_array, 'b', label='T_in')
plt.plot(t_array, T_env_array, 'g', label='T_env')
plt.legend()
plt.grid()
plt.xlabel('t [s]')
plt.ylabel('[deg C]')

plt.subplot(2, 1, 2)
plt.plot(t_array, P_array, 'm', label='P')
plt.legend()
plt.grid()
plt.xlabel('t [s]')
plt.ylabel('[W]')

# plt.savefig('plot_sim_heated_water_tank.pdf')
plt.show()


# %% Comments on the results:

print('Results and comments:')
print('Static value of P [W] = P0:', P0)
print('Static value of T [deg C]:', f'{T_array[-1]:.2f}')
print('Static value of simulated T is as specified.')

