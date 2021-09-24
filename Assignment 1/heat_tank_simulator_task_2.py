import numpy as np
import matplotlib.pyplot as plot
import math

power_init = 0  # P
power_op = 10_250  # P_op
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



def heat_tank_simulator(time_step: float = 1, start_time: float = 0, stop_time: float = 5000, power: float = 10_250, time_delay: float = 0):
    """Simulates the temperature development in a tank with a power controlled heat element.

    Args:
        time_step (float, optional): Size of time steps used by the Euler forward method. Defaults to 1 [s].
        start_time (float, optional): Start time of the simulator. Defaults to 0 [s].
        stop_time (float, optional): Stop time of the simulator. Defaults to 5000 [s].
        power (float, optional): Static power used by the simulator. Defaults to 10_250 [W].
        time_delay (float, optional): Delay before the power is turned on. Defaults to 0 [s].
    """
    # Initializing the simulator
    temperature = temp_liquid_init
    amount_of_steps = int(math.floor((stop_time-start_time)/time_step))
    print(f'{amount_of_steps = }')
    amount_of_steps_of_delay = int(
        math.floor((time_delay-start_time)/time_step))

    # initializing arrays for efficiency, using np.zeros() is a little slower but a bit safer than np.empty()
    time_array = np.zeros(amount_of_steps)
    temp_liquid_array = np.zeros(amount_of_steps)
    temp_in_array = np.zeros(amount_of_steps)
    temp_env_array = np.zeros(amount_of_steps)
    power_array = np.zeros(amount_of_steps)

    # Euler forward f(t+1) = f(t)+f'(t)*Ts
    for i in range(amount_of_steps):

        current_power = 0
        if(i >= amount_of_steps_of_delay):
            current_power = power

        current_time = i*time_step

        # Calculating temperature for this step.
        diff_temperature = (current_power+C_1*(temp_in-temperature) +
                            C_2*(temp_env-temperature))/C_3
        temperature = temperature + diff_temperature*time_step

        # Populating arrays
        time_array[i] = current_time
        temp_liquid_array[i] = temperature
        temp_in_array[i] = temp_in
        temp_env_array[i] = temp_env
        power_array[i] = current_power

    print(f'{temperature = }')

    # Plotting
    plot.close("all")  # Closes all figures before plotting
    plot.figure(num=1, figsize=(12, 9))

    # Plot 1
    plot.subplot(2, 1, 1)
    plot.plot(time_array, temp_liquid_array, "b")
    plot.plot(time_array, temp_in_array, "r")
    plot.plot(time_array, temp_env_array, "g")
    plot.grid()
    plot.xlabel("t[s]")
    plot.ylabel("[℃]")
    plot.legend(["Liquid temperature",
                "In flow temperature", "environment temperature"])

    # Plot 2
    plot.subplot(2, 1, 2)
    plot.plot(time_array, power_array, "r")
    plot.grid()
    plot.xlabel("t[s]")
    plot.ylabel("[W]")
    plot.legend(["Power"])

    # Save and show
    plot.savefig("plot_heat_tank.svg")
    plot.show()


def main():
    heat_tank_simulator(time_step=1, start_time=0,
                        stop_time=5000, power=10_250, time_delay=0)



if __name__ == "__main__":
    main()
