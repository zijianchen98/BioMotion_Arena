
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
n_points = 15

# Define the initial positions of the point lights (happy woman walking)
# These are approximate positions based on a typical human skeleton
initial_positions = np.array([
    [0.5, 0.5],  # head
    [0.4, 0.6],  # left shoulder
    [0.6, 0.6],  # right shoulder
    [0.4, 0.7],  # left elbow
    [0.6, 0.7],  # right elbow
    [0.4, 0.8],  # left hand
    [0.6, 0.8],  # right hand
    [0.5, 0.4],  # torso
    [0.5, 0.3],  # hips
    [0.4, 0.2],  # left knee
    [0.6, 0.2],  # right knee
    [0.4, 0.1],  # left ankle
    [0.6, 0.1],  # right ankle
    [0.5, 0.9],  # left foot
    [0.5, 0.0]   # right foot
])

# Define the motion parameters
# These are approximate values based on a typical human walking motion
stride_length = 0.2
stride_time = 2.0
amplitude = 0.1

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Initialize the point lights
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=50, c='white')

# Define the animation function
def animate(i):
    # Calculate the new positions of the point lights based on the motion parameters
    t = i / 50.0  # time in seconds
    phase = 2 * np.pi * t / stride_time
    positions = initial_positions.copy()
    
    # Head and torso
    positions[0, 1] = 0.5 + amplitude * np.sin(phase)
    positions[7, 1] = 0.3 + amplitude * np.sin(phase)
    
    # Shoulders and elbows
    positions[1, 1] = 0.6 + amplitude * np.sin(phase + np.pi/2)
    positions[2, 1] = 0.6 + amplitude * np.sin(phase - np.pi/2)
    positions[3, 1] = 0.7 + amplitude * np.sin(phase + np.pi)
    positions[4, 1] = 0.7 + amplitude * np.sin(phase)
    
    # Hands and feet
    positions[5, 1] = 0.8 + amplitude * np.sin(phase + np.pi/2)
    positions[6, 1] = 0.8 + amplitude * np.sin(phase - np.pi/2)
    positions[13, 1] = 0.9 + amplitude * np.sin(phase + np.pi/2)
    positions[14, 1] = 0.0 + amplitude * np.sin(phase - np.pi/2)
    
    # Hips and knees
    positions[8, 1] = 0.4 + amplitude * np.sin(phase)
    positions[9, 1] = 0.2 + amplitude * np.sin(phase + np.pi/2)
    positions[10, 1] = 0.2 + amplitude * np.sin(phase - np.pi/2)
    
    # Ankles
    positions[11, 1] = 0.1 + amplitude * np.sin(phase + np.pi/2)
    positions[12, 1] = 0.1 + amplitude * np.sin(phase - np.pi/2)
    
    # Update the x-coordinates to create the illusion of walking
    positions[:, 0] += stride_length / stride_time * t
    
    # Update the point lights
    points.set_offsets(positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=20)

plt.show()
