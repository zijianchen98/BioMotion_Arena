
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for the happy woman with heavy weight
# Each point-light is defined by its x and y coordinates
point_lights = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.8],  # Left shoulder
    [0.6, 0.8],  # Right shoulder
    [0.4, 0.7],  # Left elbow
    [0.6, 0.7],  # Right elbow
    [0.4, 0.6],  # Left hand
    [0.6, 0.6],  # Right hand
    [0.5, 0.5],  # Hips
    [0.4, 0.4],  # Left knee
    [0.6, 0.4],  # Right knee
    [0.4, 0.3],  # Left ankle
    [0.6, 0.3],  # Right ankle
    [0.5, 0.2],  # Left foot
    [0.5, 0.2],  # Right foot
    [0.5, 0.1],  # Center of mass
])

# Define the motion parameters for the running action
# Each motion parameter is defined by its amplitude, frequency, and phase
motion_params = {
    'head': {'amp': 0.1, 'freq': 2, 'phase': 0},
    'left_shoulder': {'amp': 0.2, 'freq': 2, 'phase': np.pi/2},
    'right_shoulder': {'amp': 0.2, 'freq': 2, 'phase': -np.pi/2},
    'left_elbow': {'amp': 0.3, 'freq': 4, 'phase': np.pi/2},
    'right_elbow': {'amp': 0.3, 'freq': 4, 'phase': -np.pi/2},
    'left_hand': {'amp': 0.4, 'freq': 4, 'phase': np.pi/2},
    'right_hand': {'amp': 0.4, 'freq': 4, 'phase': -np.pi/2},
    'hips': {'amp': 0.1, 'freq': 2, 'phase': 0},
    'left_knee': {'amp': 0.2, 'freq': 2, 'phase': np.pi/2},
    'right_knee': {'amp': 0.2, 'freq': 2, 'phase': -np.pi/2},
    'left_ankle': {'amp': 0.3, 'freq': 4, 'phase': np.pi/2},
    'right_ankle': {'amp': 0.3, 'freq': 4, 'phase': -np.pi/2},
    'left_foot': {'amp': 0.4, 'freq': 4, 'phase': np.pi/2},
    'right_foot': {'amp': 0.4, 'freq': 4, 'phase': -np.pi/2},
    'center_of_mass': {'amp': 0.1, 'freq': 2, 'phase': 0},
}

# Create a new figure and axis
fig, ax = plt.subplots()

# Initialize the point-lights
point_light_plots = []
for point_light in point_lights:
    point_light_plot, = ax.plot(point_light[0], point_light[1], 'wo')
    point_light_plots.append(point_light_plot)

# Set the axis limits and aspect ratio
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

# Set the background color to black
ax.set_facecolor('black')

# Define the animation function
def animate(frame):
    for i, point_light in enumerate(point_lights):
        motion_param = motion_params[list(motion_params.keys())[i]]
        point_light[0] += motion_param['amp'] * np.sin(motion_param['freq'] * frame + motion_param['phase'])
        point_light[1] += motion_param['amp'] * np.cos(motion_param['freq'] * frame + motion_param['phase'])
        point_light_plots[i].set_data(point_light[0], point_light[1])
    return point_light_plots

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), blit=True, interval=50)

# Show the animation
plt.show()
