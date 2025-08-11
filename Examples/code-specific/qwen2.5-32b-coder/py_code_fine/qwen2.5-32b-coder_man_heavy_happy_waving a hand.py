
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 30
background_color = 'black'
point_color = 'white'
fig_size = (8, 8)

# Initial positions of the point-lights (approximate)
initial_positions = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.75], [0.6, 0.75],  # Shoulders
    [0.3, 0.6], [0.7, 0.6],   # Elbows
    [0.2, 0.4], [0.8, 0.4],   # Wrists
    [0.5, 0.6],                # Spine
    [0.5, 0.4],                # Hip
    [0.4, 0.3], [0.6, 0.3],   # Knees
    [0.3, 0.2], [0.7, 0.2],   # Ankles
    [0.45, 0.25], [0.55, 0.25] # Feet
])

# Function to update the positions of the point-lights
def update(frame):
    t = frame / frames * 2 * np.pi
    positions = initial_positions.copy()
    
    # Waving motion for the right arm
    positions[4] += np.array([0.1 * np.sin(t), -0.1 * np.cos(t)])
    positions[5] += np.array([0.2 * np.sin(t), -0.2 * np.cos(t)])
    
    # Natural swaying motion for the body
    sway = 0.02 * np.sin(t / 2)
    positions[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]] += np.array([sway, 0])
    
    scatter.set_offsets(positions)
    return scatter,

# Setup figure and axis
fig, ax = plt.subplots(figsize=fig_size)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor(background_color)

# Create scatter plot for point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color=point_color)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Show animation
plt.show()
