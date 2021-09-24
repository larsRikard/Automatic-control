"""

Course FM1220 Automatic Control at USN

Compulsory assignment 1:
Programming a simulator of an heated tank in Python

Solution to Problem 4:
"Voluntary: Time delay: Set the time step to 1 sec.
Include a time delay of 60 sec in P.
Verify with a simulation that the time delay has been
implemented correctly."

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

#%% Sim time settings:

dt = 1  # [s]
t_start = 0  # [s]
t_stop = 10000  # [s]
N_sim = int((t_stop - t_start)/dt) + 1

#%% Defining a step change in power P. A step is a
# convenient test signal to demonstrate the time delay
# of the system: 

T_static = 25  # [deg C]  Static temp

# From model after t' is set to zero (static value): 
P0 = - (c*rho*F*(T_in-T_static) + U*(T_env-T_static))  # [W]

dP = 0.1*P0  # [W] Step amplitude of 10 percent
P1 = P0 + dP  # [W]  Power after step change
print('P0 [W] =', P0)
print('P1 [W] =', P1)

#%% Array for transport delay of power:

t_delay = 60  # [s]
P_delayed_init = P0  # [W]
N_delay = int(round(t_delay/dt)) + 1
P_delay_array = np.zeros(N_delay) + P_delayed_init

#%% Preallocation of arrays for storing:

t_array = np.zeros(N_sim)
T_array = np.zeros(N_sim)
T_in_array = np.zeros(N_sim)
T_env_array = np.zeros(N_sim)
P_array = np.zeros(N_sim)

#%% Sim loop:

T_k = T_init = 25  # [deg C]
t0 = 5000  # [s] Time of step in P

for k in range(0, N_sim):

    t_k = k*dt
    
    if (0 <= t_k <= t0):
        P_k = P0
        T_in_k = T_in
        T_env_k = T_env
    else:
        P_k = P1
        T_in_k = T_in
        T_env_k = T_env
    
    # Moving delay array elements one step:
    P_delayed_k = P_delay_array[-1]
    P_delay_array[1:] = P_delay_array[0:-1]
    P_delay_array[0] = P_k
    
    dT_dt_k = ((1/(c*rho*V))
               *(P_delayed_k
                 + (c*rho*F)*(T_in-T_k) 
                 + U*(T_env-T_k)))
    T_kp1 = T_k + dt*dT_dt_k
    
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

# Defining time intervals for plotting:
# Start time for plotting:
t_plot_start = 4900 #  [s]
# Stop time for plotting:
t_plot_end = 5200  # [s]
#  Array index for start of plotting:
i_start = int(t_plot_start/dt)  # [s]
# Array index for start of plotting
i_end = int(t_plot_end/dt)  # [s]
# Index interval for plotting
i_interval = np.arange(i_start, i_end, dt)

plt.subplot(2, 1, 1)
plt.plot(t_array[i_interval], T_array[i_interval], 'b',
         label='T')
plt.legend()
plt.grid()
plt.xlabel('t [s]')
plt.ylabel('[C]')

plt.subplot(2, 1, 2)
plt.plot(t_array[i_interval], P_array[i_interval], 'm', label='P')
plt.legend()
plt.grid()
plt.xlabel('t [s]')
plt.ylabel('[W]')

# plt.savefig('plot_sim_heated_water_tank.pdf')
plt.show()

# %% Comments on the results:

print('Comments:')
print('The simulation plots confirms that the',
      'time delay is 60 s.')
