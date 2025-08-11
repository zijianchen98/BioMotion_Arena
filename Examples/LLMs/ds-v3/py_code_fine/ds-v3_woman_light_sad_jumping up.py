
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rcParams

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_aspect('equal')
ax.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Define keyframes for the jumping motion (simplified)
def get_keyframe(t):
    # Time is normalized between 0 and 1 for the jump cycle
    t = t % 1.0
    
    # Key positions for a sad woman jumping
    if t < 0.1:  # Start position (standing)
        x = np.array([0, 0, 0, -0.2, 0.2, -0.15, 0.15, -0.1, 0.1, -0.3, 0.3, -0.2, 0.2, 0, 0])
        y = np.array([1.5, 1.2, 0.9, 0.7, 0.7, 0.5, 0.5, 0.3, 0.3, 0.0, 0.0, -0.2, -0.2, -0.3, -0.4])
    elif t < 0.3:  # Crouching before jump
        crouch_factor = (t - 0.1) / 0.2
        x = np.array([0, 0, 0, -0.2, 0.2, -0.15, 0.15, -0.1, 0.1, -0.3, 0.3, -0.2, 0.2, 0, 0])
        y = np.array([1.5, 1.2, 0.9 - crouch_factor * 0.2, 
                      0.7 - crouch_factor * 0.1, 0.7 - crouch_factor * 0.1,
                      0.5 - crouch_factor * 0.1, 0.5 - crouch_factor * 0.1,
                      0.3 - crouch_factor * 0.2, 0.3 - crouch_factor * 0.2,
                      0.0 - crouch_factor * 0.1, 0.0 - crouch_factor * 0.1,
                      -0.2 + crouch_factor * 0.1, -0.2 + crouch_factor * 0.1,
                      -0.3 + crouch_factor * 0.1, -0.4 + crouch_factor * 0.1])
    elif t < 0.5:  # Jumping up
        jump_factor = (t - 0.3) / 0.2
        height = jump_factor * 1.0
        x = np.array([0, 0, 0, -0.2 - jump_factor * 0.1, 0.2 + jump_factor * 0.1, 
-0.15 - jump_factor * 0.05, 0.15 + jump_factor * 0.05, 
-0.1, 0.1, -0.3, 0.3, -0.2, 0.2, 0, 0])
        y = np.array([1.5 + height, 1.2 + height, 0.9 + height - jump_factor * 0.1, 
                      0.6 + height, 0.6 + height,
                      0.4 + height, 0.4 + height,
                      0.1 + height, 0.1 + height,
                      -0.1 + height, -0.1 + height,
                      -0.1 + height, -0.1 + height,
                      -0.2 + height, -0.3 + height])
    elif t < 0.7:  # At peak of jump
        peak_factor = (t - 0.5) / 0.2
        height = 1.0 - peak_factor * 0.5
        x = np.array([0, 0, 0, -0.3 + peak_factor * 0.1, 0.3 - peak_factor * 0.1, 
                      -0.2 + peak_factor * 0.05, 0.2 - peak_factor * 0.05, 
                      -0.1, 0.1, -0.3, 0.3, -0.2, 0.2, 0, 0])
        y = np.array([1.5 + height, 1.2 + height, 0.8 + height, 
                      0.6 + height, 0.6 + height,
                      0.4 + height, 0.4 + height,
                      0.1 + height, 0.1 + height,
                      -0.1 + height, -0.1 + height,
                      -0.1 + height, -0.1 + height,
                      -0.2 + height, -0.3 + height])
    else:  # Landing
        land_factor = (t - 0.7) / 0.3
        height = 0.5 - land_factor * 0.5
        x = np.array([0, 0, 0, -0.2, 0.2, -0.15, 0.15, -0.1, 0.1, -0.3, 0.3, -0.2, 0.2, 0, 0])
        y = np.array([1.5 + height, 1.2 + height, 0.9 + height - land_factor * 0.2, 
                      0.7 + height - land_factor * 0.1, 0.7 + height - land_factor * 0.1,
                      0.5 + height - land_factor * 0.1, 0.5 + height - land_factor * 0.1,
                      0.3 + height - land_factor * 0.2, 0.3 + height - land_factor * 0.2,
                      0.0 + height - land_factor * 0.1, 0.0 + height - land_factor * 0.1,
                      -0.2 + height + land_factor * 0.1, -0.2 + height + land_factor * 0.1,
                      -0.3 + height + land_factor * 0.1, -0.4 + height + land_factor * 0.1])
    
    return x, y

# Animation update function
def update(frame):
    t = frame * 30 / 1000  # Convert frame to time (30 frames per second)
    x, y = get_keyframe(t)
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=30, blit=True)

plt.tight_layout()
plt.show()
