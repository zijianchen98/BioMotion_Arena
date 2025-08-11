
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
frames = 100
angle_increment = 2 * np.pi / frames

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initial positions of lights (simplified model of a person turning around)
angles = np.linspace(0, 2 * np.pi, num_lights, endpoint=False)
radii = np.array([0.5] * 5 + [0.4] * 5 + [0.3] * 5)  # Different radii for limbs and torso
x = radii * np.cos(angles)
y = radii * np.sin(angles)

# Scatter plot for lights
scat = ax.scatter(x, y, s=100, color='white')

def update(frame):
    global x, y
    
    # Update angles based on frame
    new_angles = angles + frame * angle_increment
    
    # Update positions
    x = radii * np.cos(new_angles)
    y = radii * np.sin(new_angles)
    
    # Apply some biomechanical constraints to make it look more like a person turning
    # Simplified: adjust the arms and legs to swing in arcs
    arm_swing = 0.2 * np.sin(2 * frame * angle_increment)
    leg_swing = 0.1 * np.sin(2 * frame * angle_increment)
    
    # Adjust the first 5 points (torso) to move in a circle
    x[:5] = 0.5 * np.cos(new_angles[:5])
    y[:5] = 0.5 * np.sin(new_angles[:5])
    
    # Adjust the next 5 points (arms) to swing
    x[5:10] += arm_swing
    y[5:10] += arm_swing
    
    # Adjust the last 5 points (legs) to swing
    x[10:] += leg_swing
    y[10:] += leg_swing
    
    scat.set_offsets(np.c_[x, y])
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, blit=True, repeat=True)

plt.show()
