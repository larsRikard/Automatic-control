#  -*- coding: utf-8 -*-
"""

Author: Finn Haugen, USN
finn.haugen@usn.no

Simulator of PI control system for process with
time constant and time delay dynamics

Implemented in Python 3.8.

Updated 2020 12 10.

"""

# %% Imports

import matplotlib.pyplot as plt
import numpy as np

# %% Function defining a PI controller:

def fun_pi_contr(y_sp_k, y_k, u_i_km1, contr_params, ts):
    
    (Kc, Ti, u_man, u_min, u_max) = contr_params
    e_k = y_sp_k - y_k  # Control error
    u_p_k = Kc*(y_sp_k - y_k)  # P term
    u_i_k = u_i_km1 + (Kc*ts/Ti)*e_k  # PI term
    u_i_min = u_min - u_man
    u_i_max = u_max - u_man
    u_i_k = np.clip(u_i_k, u_i_min, u_i_max)  # Limit ui
    u_k = u_man + u_p_k + u_i_k  # Total control signal
    u_k = np.clip(u_k, u_min, u_max)  # Limit of control
    
    return (u_k, u_i_k)

# %% Def of process model simulator

def process_sim(y_k,
                u_k,
                d_k,
                delay_array_k,
                process_params,
                ts):

    # Reading process params:
    (Ku, Kd, t_const, t_delay, y_min, y_max) = process_params
    
    # Limiting the state:
    y_k = np.clip(y_k, y_min, y_max)
    
    # Time delay:
    u_delayed_k = delay_array_k[-1]
    delay_array_k[1:] = delay_array_k[0:-1]
    delay_array_k[0] = u_k
    delay_array_kp1 = delay_array_k

    # Euler-forward integration of process state variable:
    dy_dt_k = (1/t_const)*(Ku*u_delayed_k + Kd*d_k - y_k)
    y_kp1 = y_k + ts*dy_dt_k

    return (y_k, y_kp1, delay_array_kp1)

# %% Time settings:

ts = 0.05  # Time-step [s]
t_start = 0.0  # [s]
t_stop = 100.0  # [s]
N_sim = int((t_stop - t_start)/ts) + 1

# %% Process params:

Ku = 1  # [%/%]
Kd = -1  # [%/%]
t_const = 20.0  # [s]
t_delay = 3.0  # [s]

y_min = 0  # [%]
y_max = np.inf  # [%]

process_params = (Ku, Kd, t_const, t_delay, y_min, y_max)

# %% Initialization of time delay:

u_delayed_init = 50  # [V]
N_delay = int(round(t_delay/ts)) + 1
delay_array_k = np.zeros(N_delay) + u_delayed_init


# %% PI controller settings:

Kc = 3.6
Ti = np.Infinity
u_man = 50  # [%]
u_max = 100  # [%]
u_min = 0  # [%]
contr_params = (Kc, Ti, u_man, u_min, u_max)

# %% Defining arrays for plotting:

t_array = np.zeros(N_sim)
y_array = np.zeros(N_sim)
d_array = np.zeros(N_sim)
y_sp_array = np.zeros(N_sim)
u_array = np.zeros(N_sim)

# %% Initial state:

y_k = 50.0  # [%]
u_i_km1 = 0  # [%]

# %% Simulation for-loop:

for k in range(0, N_sim):

    t_k = k*ts

    # Setting setpoint and disturbance:
    if t_k <= 10:
        y_sp_k = 50  # [%]
        d_k = 0  # [%]
    else:
        y_sp_k = 51  # [%]
        d_k = 0  # [%]
    
    # Control error:
    e_k = y_k - y_k
    
    # Controller:
    (u_k, u_i_k) = fun_pi_contr(y_sp_k, y_k, u_i_km1,
                                contr_params, ts)
    
    # Process simulator:
    (y_k, y_kp1, delay_array_kp1) = process_sim(
        y_k,
        u_k,
        d_k,
        delay_array_k,
        process_params,
        ts)
    
    # Storage for plotting:
    t_array[k] = t_k
    u_array[k] = u_k
    y_array[k] = y_k
    d_array[k] = d_k
    y_sp_array[k] = y_sp_k
    
    # Time index shift:
    y_k = y_kp1
    u_i_km1 = u_i_k
    delay_array_k = delay_array_kp1

# %% Plotting:

plt.close('all')
plt.figure(1)

plt.subplot(3, 1, 1)
plt.plot(t_array, y_sp_array, 'r', label='y_sp')
plt.plot(t_array, y_array, 'b', label='y')
plt.legend()
plt.grid()
#plt.ylim(20, 25)
plt.xlim(t_start, t_stop)
plt.xlabel('t [s]')
plt.ylabel('[%]')

plt.subplot(3, 1, 2)
plt.plot(t_array, u_array, 'm', label='u')
plt.legend()
plt.grid()
#plt.ylim(-1, 6)
plt.xlim(t_start, t_stop)
plt.xlabel('t [s]')
plt.ylabel('[%]')

plt.subplot(3, 1, 3)
plt.plot(t_array, d_array, 'g', label='d')
plt.legend()
plt.grid()
#plt.ylim(-1, 6)
plt.xlim(t_start, t_stop)
plt.xlabel('t [s]')
plt.ylabel('[%]')

# plt.savefig('sim_pi_control_sys.pdf')
plt.show()