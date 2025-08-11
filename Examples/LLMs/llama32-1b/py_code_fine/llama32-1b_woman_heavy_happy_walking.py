
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
WIDTH, HEIGHT = 800, 600
WHITE_COLOR = (1, 1, 1)
BLACK_COLOR = (0, 0, 0)
WEIGHT_COLOR = (0.8, 0.8, 0.8)

# Define the subject and action
SUBJECT = "woman"
ACTION = "walking"

# Define the parameters for the animation
N_STEPS = 100
TSTEP = 0.01
dt = TSTEP

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_axis_off()

# Initialize the points and velocities
points = np.zeros((N_STEPS, 2))
velocities = np.zeros((N_STEPS, 2))

# Define the initial position and velocity of the subject
initial_position = np.array([WIDTH / 2, HEIGHT / 2])
initial_velocity = np.array([0, 0])

# Define the parameters for the point-lights
light_positions = np.array([[WIDTH / 2, HEIGHT / 2]])
light_velocities = np.array([[0, 0]])

# Function to update the points and velocities
def update(frame):
    global points, velocities, light_positions, light_velocities
    
    # Update the positions of the points
    points[:, 0] += velocities[:, 0] * dt
    points[:, 1] += velocities[:, 1] * dt
    
    # Update the velocities of the points
    velocities[:, 0] += light_velocities * dt
    velocities[:, 1] += light_velocities * dt
    
    # Update the positions of the lights
    light_positions[:, 0] += light_velocities[:, 0] * dt
    light_positions[:, 1] += light_velocities[:, 1] * dt
    
    # Plot the points and lights
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_axis_off()
    
    # Plot the points
    for i in range(N_STEPS):
        ax.plot(points[i, 0], points[i, 1], 'k-')
    
    # Plot the lights
    for i in range(N_STEPS):
        ax.scatter(light_positions[i, 0], light_positions[i, 1], color=WHITE, s=10)
    
    # Plot the subject
    ax.scatter(initial_position[0], initial_position[1], color=WHITE, s=50)
    
    # Update the plot
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_axis_off()
    plt.pause(0.01)

# Animate the subject
ani = animation.FuncAnimation(fig, update, frames=N_STEPS, interval=100, blit=True)

plt.show()
