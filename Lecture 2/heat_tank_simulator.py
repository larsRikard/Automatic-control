import numpy as np
import matplotlib.pyplot as plot
import math

power_init = 0                      #P
power_op = 10_250                   #P_op
temp_liquid_init = 20               #T
temp_env = 20                       #T_env
temp_in = 20                        #T_in
flow = 0.25*10**(-3)                #F
specific_heat_capacity = 4200       #c
density = 1000                      #ρ
volume_tank = 0.2                   #V
heat_transfer_coefficient = 1000    #U
time_delay = 60                     #τ

C_1 = specific_heat_capacity*density*flow           #c*ρ*F
C_2 = heat_transfer_coefficient                     #U
C_3 = specific_heat_capacity*density*volume_tank    #C*ρ*v

#asdf

def heat_tank_simulator(time_step: float, start_time: float, stop_time: float, power: float):
    temperature = temp_liquid_init
    resolution = int(math.floor((stop_time-start_time)/time_step))
    print(f'{resolution = }')
    print(f'{C_3 = }')

    for i in range(resolution):
        diff_temperature = (power+C_1*(temp_in-temperature)+C_2*(temp_env-temperature))/C_3
        temperature = temperature + diff_temperature*time_step
    print(f'{temperature = }')

heat_tank_simulator(1,0,100_000, power_op)