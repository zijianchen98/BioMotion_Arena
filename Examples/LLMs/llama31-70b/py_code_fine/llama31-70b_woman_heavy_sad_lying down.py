
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for the sad woman
point_lights = np.array([
    [0.5, 0.5],  # head
    [0.4, 0.6],  # left shoulder
    [0.6, 0.6],  # right shoulder
    [0.4, 0.7],  # left elbow
    [0.6, 0.7],  # right elbow
    [0.4, 0.8],  # left hand
    [0.6, 0.8],  # right hand
    [0.5, 0.4],  # torso
    [0.4, 0.5],  # left hip
    [0.6, 0.5],  # right hip
    [0.4, 0.3],  # left knee
    [0.6, 0.3],  # right knee
    [0.4, 0.2],  # left ankle
    [0.6, 0.2],  # right ankle
    [0.5, 0.9]   # weight
])

# Define the movement of each point-light for the lying down action
def animate(frame):
    animated_point_lights = point_lights.copy()
    
    # Move the head
    animated_point_lights[0, 1] = 0.5 + 0.1 * np.sin(frame / 10.0)
    
    # Move the shoulders
    animated_point_lights[1, 1] = 0.6 + 0.05 * np.sin(frame / 10.0)
    animated_point_lights[2, 1] = 0.6 - 0.05 * np.sin(frame / 10.0)
    
    # Move the elbows
    animated_point_lights[3, 1] = 0.7 + 0.05 * np.sin(frame / 10.0)
    animated_point_lights[4, 1] = 0.7 - 0.05 * np.sin(frame / 10.0)
    
    # Move the hands
    animated_point_lights[5, 1] = 0.8 + 0.05 * np.sin(frame / 10.0)
    animated_point_lights[6, 1] = 0.8 - 0.05 * np.sin(frame / 10.0)
    
    # Move the torso
    animated_point_lights[7, 1] = 0.4 + 0.05 * np.sin(frame / 10.0)
    
    # Move the hips
    animated_point_lights[8, 1] = 0.5 + 0.05 * np.sin(frame / 10.0)
    animated_point_lights[9, 1] = 0.5 - 0.05 * np.sin(frame / 10.0)
    
    # Move the knees
    animated_point_lights[10, 1] = 0.3 + 0.05 * np.sin(frame / 10.0)
    animated_point_lights[11, 1] = 0.3 - 0.05 * np.sin(frame / 10.0)
    
    # Move the ankles
    animated_point_lights[12, 1] = 0.2 + 0.05 * np.sin(frame / 10.0)
    animated_point_lights[13, 1] = 0.2 - 0.05 * np.sin(frame / 10.0)
    
    # Move the weight
    animated_point_lights[14, 1] = 0.9 + 0.05 * np.sin(frame / 10.0)
    
    return animated_point_lights

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot
point_light_plots = ax.scatter(point_lights[:, 0], point_lights[:, 1], s=50, c='w')

# Set the plot limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Set the background color to black
ax.set_facecolor('k')

# Remove the axis ticks
ax.set_xticks([])
ax.set_yticks([])

# Define the animation function
def animate_point_lights(frame):
    animated_point_lights = animate(frame)
    point_light_plots.set_offsets(animated_point_lights)
    return point_light_plots,

# Create the animation
ani = animation.FuncAnimation(fig, animate_point_lights, frames=range(100), blit=True, interval=50)

plt.show()
