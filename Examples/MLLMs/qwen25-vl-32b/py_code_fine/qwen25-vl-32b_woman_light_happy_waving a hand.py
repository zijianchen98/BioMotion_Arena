
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
initial_positions = {
    'head': [0, 0],
    'torso': [0, -1],
    'left_shoulder': [-0.5, -1.5],
    'right_shoulder': [0.5, -1.5],
    'left_elbow': [-1, -2.5],
    'right_elbow': [1, -2.5],
    'left_wrist': [-1.5, -3.5],
    'right_wrist': [1.5, -3.5],
    'left_hip': [-0.5, -2],
    'right_hip': [0.5, -2],
    'left_knee': [-1, -3],
    'right_knee': [1, -3],
    'left_ankle': [-1.5, -4],
    'right_ankle': [1.5, -4],
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Define the wave amplitude and frequency for the right hand
wave_amplitude = 0.5
wave_frequency = 0.5  # Hz

# Function to update the positions based on time
def update_positions(t):
    updated_coords = initial_coords.copy()
    
    # Wave the right hand (right wrist)
    updated_coords[7][1] += wave_amplitude * np.sin(2 * np.pi * wave_frequency * t)
    
    return updated_coords

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-5, 1)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point lights
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    t = frame / 30  # Assuming 30 frames per second
    positions = update_positions(t)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=360, interval=33, blit=True  # 30 FPS
)

# Display the animation
plt.show()
