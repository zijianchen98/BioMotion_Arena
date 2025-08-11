
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights representing the sad man's joints
point_lights = np.array([
    [-0.2, 0.5],  # Head
    [-0.1, 0.4],  # Right shoulder
    [0.1, 0.4],   # Left shoulder
    [-0.2, 0.2],  # Right elbow
    [0.2, 0.2],   # Left elbow
    [-0.3, 0.0],  # Right hand
    [0.3, 0.0],   # Left hand
    [0.0, 0.3],   # Right hip
    [0.0, 0.2],   # Left hip
    [-0.2, -0.1], # Right knee
    [0.2, -0.1],  # Left knee
    [-0.3, -0.3], # Right ankle
    [0.3, -0.3],  # Left ankle
    [0.0, -0.2],  # Right foot
    [0.0, -0.1]   # Left foot
])

# Define the walking motion
def walking_motion(t):
    # Calculate the positions of the point-lights at time t
    positions = np.zeros((15, 2))
    positions[0] = [0, 0.5 + 0.1 * np.sin(t)]  # Head
    
    # Shoulders
    positions[1] = [-0.1, 0.4 + 0.05 * np.sin(t)]
    positions[2] = [0.1, 0.4 + 0.05 * np.sin(t + np.pi)]
    
    # Elbows
    positions[3] = [-0.2 + 0.1 * np.sin(t), 0.2 + 0.05 * np.sin(t)]
    positions[4] = [0.2 + 0.1 * np.sin(t + np.pi), 0.2 + 0.05 * np.sin(t + np.pi)]
    
    # Hands
    positions[5] = [-0.3 + 0.2 * np.sin(t), 0.0 + 0.1 * np.sin(t)]
    positions[6] = [0.3 + 0.2 * np.sin(t + np.pi), 0.0 + 0.1 * np.sin(t + np.pi)]
    
    # Hips
    positions[7] = [0.0, 0.3 + 0.05 * np.sin(t)]
    positions[8] = [0.0, 0.2 + 0.05 * np.sin(t + np.pi)]
    
    # Knees
    positions[9] = [-0.2 + 0.1 * np.sin(t), -0.1 + 0.05 * np.sin(t)]
    positions[10] = [0.2 + 0.1 * np.sin(t + np.pi), -0.1 + 0.05 * np.sin(t + np.pi)]
    
    # Ankles
    positions[11] = [-0.3 + 0.2 * np.sin(t), -0.3 + 0.1 * np.sin(t)]
    positions[12] = [0.3 + 0.2 * np.sin(t + np.pi), -0.3 + 0.1 * np.sin(t + np.pi)]
    
    # Feet
    positions[13] = [0.0, -0.2 + 0.05 * np.sin(t)]
    positions[14] = [0.0, -0.1 + 0.05 * np.sin(t + np.pi)]
    
    return positions

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-lights
point_light_positions = walking_motion(0)
point_lights_plot = ax.scatter(point_light_positions[:, 0], point_light_positions[:, 1], s=50, c='white')

# Define the animation function
def animate(t):
    point_light_positions = walking_motion(t)
    point_lights_plot.set_offsets(point_light_positions)
    return point_lights_plot,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 2*np.pi, 128), blit=True, interval=50)

plt.show()
