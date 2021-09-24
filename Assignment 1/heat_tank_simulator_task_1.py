import numpy as np
import matplotlib.pyplot as plot
import math

power_init = 0  # P
power_op = None  # P_op
temp_liquid_init = 20  # T
temp_env = 20  # T_env
temp_in = 20  # T_in
flow = 0.25*10**(-3)  # F
specific_heat_capacity = 4200  # c
density = 1000  # ρ
volume_tank = 0.2  # V
heat_transfer_coefficient = 1000  # U
time_delay = 60  # τ

C_1 = specific_heat_capacity*density*flow  # c*ρ*F
C_2 = heat_transfer_coefficient  # U
C_3 = specific_heat_capacity*density*volume_tank  # C*ρ*v



if __name__ == "__main__":
    temp_static = 25
    power_op = -((specific_heat_capacity*density*flow*(temp_in-temp_static)) + heat_transfer_coefficient*(temp_env-temp_static))
    print(f'{power_op = }')