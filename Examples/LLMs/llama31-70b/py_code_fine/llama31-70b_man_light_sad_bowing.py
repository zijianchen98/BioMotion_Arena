
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for the sadman
point_lights = np.array([
    [0.5, 0.8],  # Head
    [0.4, 0.7],  # Left shoulder
    [0.6, 0.7],  # Right shoulder
    [0.4, 0.6],  # Left elbow
    [0.6, 0.6],  # Right elbow
    [0.4, 0.5],  # Left hand
    [0.6, 0.5],  # Right hand
    [0.5, 0.4],  # Torso
    [0.4, 0.3],  # Left hip
    [0.6, 0.3],  # Right hip
    [0.4, 0.2],  # Left knee
    [0.6, 0.2],  # Right knee
    [0.4, 0.1],  # Left ankle
    [0.6, 0.1],  # Right ankle
    [0.5, 0.05],  # Feet
])

# Define the bowing motion
def bowing_motion(t):
    t = t / 10.0  # Adjust the speed of the motion
    motion = np.zeros((15, 2))
    
    # Head
    motion[0, 1] = 0.8 - 0.1 * np.sin(t)
    
    # Shoulders
    motion[1, 1] = 0.7 - 0.05 * np.sin(t)
    motion[2, 1] = 0.7 - 0.05 * np.sin(t)
    
    # Elbows
    motion[3, 1] = 0.6 - 0.1 * np.sin(t)
    motion[4, 1] = 0.6 - 0.1 * np.sin(t)
    
    # Hands
    motion[5, 1] = 0.5 - 0.15 * np.sin(t)
    motion[6, 1] = 0.5 - 0.15 * np.sin(t)
    
    # Torso
    motion[7, 1] = 0.4 - 0.05 * np.sin(t)
    
    # Hips
    motion[8, 1] = 0.3 - 0.05 * np.sin(t)
    motion[9, 1] = 0.3 - 0.05 * np.sin(t)
    
    # Knees
    motion[10, 1] = 0.2 - 0.1 * np.sin(t)
    motion[11, 1] = 0.2 - 0.1 * np.sin(t)
    
    # Ankles
    motion[12, 1] = 0.1 - 0.05 * np.sin(t)
    motion[13, 1] = 0.1 - 0.05 * np.sin(t)
    
    # Feet
    motion[14, 1] = 0.05 - 0.05 * np.sin(t)
    
    return motion + point_lights

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the plot with the initial point-light locations
scatter = ax.scatter(point_lights[:, 0], point_lights[:, 1], c='white')

# Define the animation function
def animate(t):
    motion = bowing_motion(t)
    scatter.set_offsets(motion)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
