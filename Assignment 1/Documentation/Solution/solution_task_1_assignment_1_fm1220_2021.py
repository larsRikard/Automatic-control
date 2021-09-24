"""

Course FM1220 Automatic Control at USN

Compulsory assignment 1:
Programming a simulator of an heated tank in Python

Solution to Problem 1:
"Calculation of static operating point:
Calculate from the model the constant power, P0, needed
to bring the temperature to a constant value of 25 deg C."

Finn Aakre Haugen
finn.haugen@usn.no

2021 09 01

"""

#%% Model params:

c = 4200 # [J/(kg*K)]
rho = 1000 # [kg/m3]
V = 0.2 # [m3]
U = 1000 # [W/K]
F = 0.25e-3  # [m3/s]
T_in = 20  # [deg C]
T_env = 20  # [deg C]

#%% Calculation of power giving specified static temp: 

T_static = 25  # [deg C]  Static temp

# From model after t' is set to zero (static value): 
P0 = - (c*rho*F*(T_in-T_static) + U*(T_env-T_static))  # [W]
print('P0 [W] =', P0)
