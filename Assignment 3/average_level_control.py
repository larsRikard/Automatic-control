import math
from matplotlib import pyplot as plot
import numpy as np

# constants
tank_area = 2000  # square meter
# set point
set_point = 1  # meter

# initial conditions
initial_level = 1  # meter
flow_in = 3.0  # cubic meter / second
flow_out = 3.0  # cubic meter / second

# assumptions
delta_flow_in_max = 1.0  # cubic meter / second
delta_h_max = 0.5  # meter

T_c = (tank_area*delta_h_max)/delta_flow_in_max
T_i = 2*T_c
K_i = -1/tank_area
K_c = -tank_area/T_c
print(f'{T_c = }, {T_i = }, {K_i = }, {K_c = }')

def pi_control(prev_u_i, level, set_point, time_step):
    error = set_point-level
    u_p = K_c*error
    u_i = prev_u_i + (K_c*time_step/T_i)*error
    return u_p, u_i


def flow_in_function(time, amplitude=1, period=1200):
    return 2+(amplitude*math.sin(time*((2*math.pi)/period)))


def average_level_control(time_step: float = 1, start_time: float = 0, stop_time: float = 5000, time_delay: float = 0):
    # Initializing the simulator
    amount_of_steps = int(math.floor((stop_time-start_time)/time_step))
    amount_of_steps_of_delay = int(
        math.floor((time_delay-start_time)/time_step))

    # initializing arrays for efficiency, using np.zeros() is a little slower but a bit safer than np.empty()
    time_array = np.zeros(amount_of_steps)
    time_array[0] = 0
    level_set_point_array = np.full(amount_of_steps,set_point)
    level_array = np.zeros(amount_of_steps)
    level_array[0] = initial_level
    flow_in_array = np.zeros(amount_of_steps)
    flow_in_array[0] = flow_in_function(0)
    flow_out_array = np.zeros(amount_of_steps)
    flow_out_array[0] = 3
    diff_level_array = np.zeros(amount_of_steps)

    # initializing the pid integrator
    u_i = 0

    for i in range(1, amount_of_steps):
        time_array[i] = i*time_step
        u_p, u_i = pi_control(u_i, level_array[i-1], set_point, time_step)
        u = u_p + u_i
        if(i >= amount_of_steps_of_delay):
            flow_in_array[i] = flow_in_function(time_array[i])
            flow_out_array[i] = u
            diff_level_array[i] = flow_in_array[i]-flow_out_array[i]
            level_array[i] = level_array[i-1]+diff_level_array[i]*time_step

    fig = plot.figure()
    plot.figure(num=1, figsize=(12, 9))
    
    plot.subplot(2, 1, 1)
    l1, l2 = plot.plot(time_array, level_array, time_array, level_set_point_array)
    fig.legend((l1, l2), ('Level', 'Level_set_point'), "upper left")
    plot.xlabel('time')

    plot.subplot(2, 1, 2)
    l3, l4 = plot.plot(time_array,flow_in_array, time_array,flow_out_array)
    fig.legend((l3,l4), ('In flow','Out flow'))
    plot.xlabel('time')

    plot.show()



if __name__ == "__main__":
    average_level_control()