import numpy as np
import matplotlib.pyplot as plt

# Define the A matrix
A = np.array([[-1, -1], [1, -1]])
B = np.array([-1, 0]) 

# Define the system dynamics as a function of state and control input
def system_dynamics(x, u):

    Ax = np.dot(A, x)
    Bx = B * u
    return  Ax + Bx

# Euler method simulation
def euler_method(initial_state, control_input, T, dt):
    num_steps = int(T / dt)
    states = [initial_state]
    t = 0

    for _ in range(num_steps):
        x = states[-1]
        u = control_input(t)

        dxdt = system_dynamics(x, u)

        x_new = x + dxdt * dt
        states.append(x_new)
        t += dt

    return states

# Define the initial state, control input, simulation time, and time step
initial_state = np.array([1, 1])  # Initial state [x1(0), x2(0)]
T = 10.0  # Total simulation time
dt = 0.001  # Time step

# Define a control input function (e.g., a constant control input)
def constant_control_input(t):
    return 0.0  # Replace with your control input profile

# Simulate the system
simulated_states = euler_method(initial_state, constant_control_input, T, dt)


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