from matplotlib import pyplot as plot
import numpy as np

# constants
tank_area = 2000  # square meter
# set point
set_point = 1  # meter

# initial conditions
initial_level = 1  # meter
flow_in = 2.0  # cubic meter / second
flow_out = 2.0  # cubic meter / second

# assumptions
delta_flow_in_max = 1.0  # cubic meter / second
delta_h_max = 0.5  # meter

T_c = (tank_area*delta_h_max)/delta_flow_in_max
T_i = 2*T_c
K_i = -1/tank_area
K_c = 1/(K_i*T_c)
print(f'{T_c = }, {T_i = }, {K_i = }, {K_c = }')


def pi_control(prev_u_i, error, time_step):
    #print(f'{prev_u_i = }, {error = }, {K_c = }, {time_step = }, {T_i = }')
    u_p = K_c*error
    u_i = prev_u_i + (K_c*time_step/T_i)*error
    return u_p, u_i


def flow_in_function(time, amplitude=1, period=1200):
    return 3+(amplitude*np.sin(time*((2*np.pi)/period)))


def average_level_control(time_step: float = 0.1, start_time: float = 0, stop_time: float = 10000, time_delay: float = 0):
    # Initializing the simulator
    amount_of_steps = int(np.floor((stop_time-start_time)/time_step))
    amount_of_steps_of_delay = int(
        np.floor((time_delay-start_time)/time_step))

    time_array = np.zeros(amount_of_steps)
    time_array[0] = 0

    level_set_point_array = np.full(amount_of_steps, set_point)

    level_array = np.zeros(amount_of_steps)
    level_array[0] = initial_level

    flow_in_array = np.zeros(amount_of_steps)
    flow_in_array[0] = flow_in

    flow_out_array = np.zeros(amount_of_steps)
    flow_out_array[0] = flow_out

    diff_level_array = np.zeros(amount_of_steps)
    error_array = np.zeros(amount_of_steps)
    error_array[0] = set_point-level_array[0]



    # initializing the pid integrator
    u_i = 0

    for i in range(1, amount_of_steps):
        time_array[i] = i*time_step
        u_p, u_i = pi_control(u_i, error_array[i-1], time_step)
        u = u_p + u_i
        if(i >= amount_of_steps_of_delay):
            flow_in_array[i] = flow_in_function(time_array[i])
            flow_out_array[i] = u
            diff_level_array[i] = (flow_in_array[i]-flow_out_array[i])/tank_area
            level_array[i] = level_array[i-1]+diff_level_array[i]*time_step
            error_array[i] = set_point-level_array[i]


    fig = plot.figure()
    plot.figure(num=1, figsize=(12, 9))

    plot.subplot(3, 1, 1)
    l1, l2 = plot.plot(time_array, level_array,
                       time_array, level_set_point_array)
    fig.legend((l1, l2), ('Level', 'Level_set_point'), "upper right")

    plot.subplot(3, 1, 2)
    l3, l4 = plot.plot(time_array, flow_in_array, time_array, flow_out_array)
    fig.legend((l3, l4), ('In flow', 'Out flow'), "center right")
    print(f'{flow_in_array[-100:]}')
    print(f'{flow_out_array[-100:]}')

    plot.subplot(3, 1, 3)
    l5 = plot.plot(time_array, error_array)
    fig.legend((l5), ('error'), "lower right")

    plot.show()


if __name__ == "__main__":
    average_level_control()
