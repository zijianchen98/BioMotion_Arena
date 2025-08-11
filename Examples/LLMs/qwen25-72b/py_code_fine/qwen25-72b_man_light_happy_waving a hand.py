
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the happy man
points = {
    'head': [0, 1],
    'shoulder_l': [-0.5, 0.75],
    'shoulder_r': [0.5, 0.75],
    'elbow_l': [-0.75, 0.5],
    'elbow_r': [0.75, 0.5],
    'wrist_l': [-1, 0.25],
    'wrist_r': [1, 0.25],
    'hip_l': [-0.5, -0.25],
    'hip_r': [0.5, -0.25],
    'knee_l': [-0.5, -0.75],
    'knee_r': [0.5, -0.75],
    'ankle_l': [-0.5, -1.25],
    'ankle_r': [0.5, -1.25],
    'hand_l': [-1.25, 0],
    'hand_r': [1.25, 0]
}

# Convert points to a list of coordinates
point_coords = np.array([points[key] for key in points])

# Define the waving hand motion
def update_waving(frame):
    angle = frame * np.pi / 180  # Convert frame to angle in radians
    wave_amplitude = 0.5
    wave_frequency = 0.1
    
    # Update the position of the left hand
    point_coords[6] = [-1 + wave_amplitude * np.sin(angle * wave_frequency), 0.25 + wave_amplitude * np.cos(angle * wave_frequency)]
    
    # Update the position of the wrist
    point_coords[4] = [-1 + wave_amplitude * np.sin(angle * wave_frequency) * 0.5, 0.5 + wave_amplitude * np.cos(angle * wave_frequency) * 0.5]
    
    scatter.set_offsets(point_coords)
    return scatter,

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
scatter = ax.scatter(point_coords[:, 0], point_coords[:, 1], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update_waving, frames=np.arange(0, 360, 5), interval=50, blit=True)

plt.show()
