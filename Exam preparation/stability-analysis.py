'''

Frequency response based stability analysis of
level control system of wood chip tank
using Python Control Package

Finn Aakre Haugen (finn.haugen@usn.no)

Updated 2020 12 10

'''

# %% Imports:

import numpy as np
import control
import matplotlib.pyplot as plt

# %% Creating controller transfer function:

Kc = 6.15*0.45
Ti = 1000/1.2  # [s]

C = control.tf([Kc*Ti, Kc],[Ti, 0])

# %% Process transfer function:

# Transfer function of time delay repr by Pade approx:
t_delay = 250.0  # [s]
n_pade = 5
(num_pade, den_pade) = control.pade(t_delay, n_pade)
D = control.tf(num_pade, den_pade)

# Transfer function of process model without time delay:
rho = 145  # [kg/m^3]
A = 6.7  # [m^2]
P_without_delay = control.tf([1], [(rho*A), 0])

# Resulting process transfer function:
P = control.series(D, P_without_delay)

#%% Control system transfer functions:

# Loop transfer function:
L = control.series(C, P)
# print('L(s) =', L)

# Tracking transfer function:
T = control.feedback(L)
# print('T =', T)

# %% Simulation of step response of T(s):

plt.close('all')
figsize=(12, 9)  # Inches on paper printout(?)

dt = 1  # Time-step [s]
t_start = 0.0  # [s]
t_stop = 8000.0  # [s]
t_array = np.arange(t_start, t_stop+dt, dt)    

(t_array, ym_array) = control.step_response(T, t_array)

y_sp = 1

plt.figure(1, figsize)
plt.plot(t_array, ym_array*0+y_sp, 'r', label='y_sp')
plt.plot(t_array, ym_array, 'b', label='y_m')
plt.title('Sim of response in ym due to step in y_sp')
plt.legend()
plt.grid()
plt.xlabel('t [s]')
plt.ylabel('[m]')

# %% Bode plot of loop transf fun with stability measures:

# Frequencies for Bode plot:
w0 = 0.0001  # [rad/s]
w1 = 0.01
dw = 0.0001
w = np.arange(w0, w1, dw)

plt.figure(3, figsize)

# Bode plot:
(mag, phase_rad, w) = control.bode_plot(L, w,
                                        dB=True,
                                        deg=True,
                                        margins=True,
                                        grid=True)

plt.show()