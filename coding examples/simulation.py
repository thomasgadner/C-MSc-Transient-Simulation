import numpy as np
import pwm
import matplotlib.pyplot as plt
import solver_4th as solver




def switch_manager(step, pwm_carrier, D, B_SW, B_DC):
    # Check if the PWM signal is 1.0
    if pwm.pwm(step, pwm_carrier , D) == 1.0:
        B = B_SW #If the PWM signal is 1.0, use the input vector B_SW
    else:
        B = B_DC #If the PWM signal is 0.0, use the input vector B_DC

    return B



if __name__=="__main__":
    # Define the simulation time and step size
    pwm_freq = 20e3  # PWM frequency (Hz)

    # Define the simulation time and step size
    t_end = T = 100*(1/pwm_freq);  
    # Select the discrete time step size
    dt = 1e-6  # Time step size (seconds)


    ## Initialize the state-space matrices and other variables
    D = 0.50 # Duty cycle

    # Define circuit parameters
    L = 750e-6   # Inductor value (Henry)
    C = 6.6e-6   # Capacitor value (Farad)
    R = 5        # Load resistance (Ohm)
    Vin = 24.0   # Input voltage (Volts)

    # Define state-space matrices for the buck converter
    A = np.array([[0, -1/L],[1/C, -1/(R*C)]])   # System matrix
    B_SW = np.array([1/(L),0]) # Input matrix for the switching action
    B_DC = np.array([0, 0]) #Input matrix for the Diode condution action

    # Define the initial state vector with the initial condition 
    initial_inductor_current = 0.0  # Initial inductor current (A)
    initial_capacitor_voltage = 0.0  # Initial capacitor voltage (V)

    # Initial state [x1(0), x2(0)]
    initial_state = np.array([initial_inductor_current, initial_capacitor_voltage])  


    # Define the PWM and carrier signal
    t = np.arange(0,t_end,dt)  # time vector for carrier and pwm
    pwm_carrier = pwm.carrier(t,pwm_freq,centeraligned=True) # Center-aligned carrier signal

    # Define the initial state vector with the initial condition
    sim_states = [initial_state]

    # Start the simulation
    for step in range(0, len(t)-1):

        # Here acontinuous control input for the Duyty cycle can be implemented

        peak_current_coroller()

        # Call the switch manager function
        B = switch_manager(step, pwm_carrier, D, B_SW, B_DC)

        # Update the state vector using the Runge-Kutta 4th order method, call the solver function
        sim_states.append(solver.runge_kutta_4th_order_extern(A, B, sim_states, Vin, dt))
        # Append the new state vector to the states list
        


    # Extract x1 and x2 values for the phase plot
    i_L = [state[0] for state in sim_states]
    v_C = [state[1] for state in sim_states]

    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(t, v_C ,t, i_L)
    plt.xlabel('t')
    plt.ylabel('v_C')
    plt.title('Output voltage and inductor current')
    plt.grid(True)
    plt.legend()
    plt.show()






    percent=30.0
TimePeriod=1.0
Cycles=10
dt=0.01 

t=np.arange(0,Cycles*TimePeriod,dt); 
pwm= t%TimePeriod<TimePeriod*percent/100 
plot(t,pwm)