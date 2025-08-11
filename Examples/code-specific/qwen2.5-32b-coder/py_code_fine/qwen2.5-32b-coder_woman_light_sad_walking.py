
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 24
background_color = 'black'
point_color = 'white'
fig_size = (8, 8)

# Initialize positions for the point lights
positions = np.zeros((frames, num_lights, 2))

# Define the walking motion for each point light
def walk_motion(t, x0, y0, phase, freq, amp_x, amp_y):
    x = x0 + amp_x * np.sin(freq * t + phase)
    y = y0 + amp_y * np.cos(freq * t + phase)
    return x, y

# Set initial positions and parameters for each point light
params = [
    (0.5, 0.5, 0, 2*np.pi/frames, 0.1, 0.1),  # Head
    (0.4, 0.4, np.pi/4, 2*np.pi/frames, 0.05, 0.05),  # Left shoulder
    (0.6, 0.4, -np.pi/4, 2*np.pi/frames, 0.05, 0.05),  # Right shoulder
    (0.3, 0.3, np.pi/2, 2*np.pi/frames, 0.05, 0.05),  # Left elbow
    (0.7, 0.3, -np.pi/2, 2*np.pi/frames, 0.05, 0.05),  # Right elbow
    (0.2, 0.2, 3*np.pi/4, 2*np.pi/frames, 0.05, 0.05),  # Left hand
    (0.8, 0.2, -3*np.pi/4, 2*np.pi/frames, 0.05, 0.05),  # Right hand
    (0.5, 0.3, 0, 2*np.pi/frames, 0.05, 0.05),  # Spine top
    (0.5, 0.2, 0, 2*np.pi/frames, 0.05, 0.05),  # Spine middle
    (0.5, 0.1, 0, 2*np.pi/frames, 0.05, 0.05),  # Spine bottom
    (0.4, 0.1, np.pi/4, 2*np.pi/frames, 0.05, 0.05),  # Left hip
    (0.6, 0.1, -np.pi/4, 2*np.pi/frames, 0.05, 0.05),  # Right hip
    (0.3, 0.0, np.pi/2, 2*np.pi/frames, 0.05, 0.05),  # Left knee
    (0.7, 0.0, -np.pi/2, 2*np.pi/frames, 0.05, 0.05),  # Right knee
    (0.4, -0.1, 3*np.pi/4, 2*np.pi/frames, 0.05, 0.05),  # Left foot
    (0.6, -0.1, -3*np.pi/4, 2*np.pi/frames, 0.05, 0.05)   # Right foot
]

for i in range(num_lights):
    x0, y0, phase, freq, amp_x, amp_y = params[i]
    for t in range(frames):
        positions[t, i] = walk_motion(t, x0, y0, phase, freq, amp_x, amp_y)

# Create the plot
fig, ax = plt.subplots(figsize=fig_size, facecolor=background_color)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Initialize scatter plot
scatter = ax.scatter([], [], s=100, c=point_color)

# Update function for animation
def update(frame):
    scatter.set_offsets(positions[frame])
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Show the animation
plt.show()
