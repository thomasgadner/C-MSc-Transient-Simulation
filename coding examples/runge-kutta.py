import numpy as np
import matplotlib.pyplot as plt



# Define the system dynamics as a function of state and control input
def system_dynamics(A, B, x, u):
    return  A @ x + B * u


# Runge-Kutta 4th order method simulation
def runge_kutta_4th_order_extern(A, B, states, input, dt):
    x = states[-1]
    u = input

    k1 = system_dynamics(A, B, x, u)
    k2 = system_dynamics(A, B, x + 0.5 * dt * k1, u)
    k3 = system_dynamics(A, B, x + 0.5 * dt * k2, u)
    k4 = system_dynamics(A, B, x + dt * k3, u)

    return x + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    
    



# Runge-Kutta 4th order method simulation
def runge_kutta_4th_order(A, B, initial_state, control_input, T, dt):
    num_steps = int(T / dt)
    states = [initial_state]
    t = 0

    for _ in range(num_steps):
        x = states[-1]
        u = control_input(t)

        k1 = system_dynamics(A, B, x, u)
        k2 = system_dynamics(A, B, x + 0.5 * dt * k1, u)
        k3 = system_dynamics(A, B, x + 0.5 * dt * k2, u)
        k4 = system_dynamics(A, B, x + dt * k3, u)

        x_new = x + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        states.append(x_new)
        t += dt

    return states



# Define a control input function (e.g., a constant control input)
def constant_control_input(t):
    return 0.0  # Replace with your control input profile


if __name__=="__main__":

    # Define the A matrix
    A = np.array([[-1, -1], [1, -1]])
    B = np.array([-1, 0])

    # Define the initial state, control input, simulation time, and time step
    initial_state = np.array([1, 1])  # Initial state [x1(0), x2(0)]
    T = 10.0  # Total simulation time
    dt = 0.2  # Time step

    # Simulate the system using Runge-Kutta 4th order
    simulated_states = runge_kutta_4th_order(A, B, initial_state, constant_control_input, T, dt)

    # Extract x1 and x2 values for the phase plot
    i_L = [state[0] for state in simulated_states]
    v_C = [state[1] for state in simulated_states]

    # Create a phase plot
    plt.figure(figsize=(8, 6))
    plt.plot(v_C, i_L, label='Phase Plot')
    plt.xlabel('i_L')
    plt.ylabel('v_C')
    plt.title('Phase Plot')
    plt.grid(True)
    plt.legend()
    plt.show()
