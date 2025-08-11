
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights and figure settings
num_points = 15
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
point_lights, = ax.plot([], [], 'o', color='white')

# Define the initial positions of the point lights for a 'bowing' posture
# Using a simple approach where the lights are positions of key joints
def init():
    point_lights.set_data([], [])
    return point_lights,

# Define the updating function for animation
def update(frame):
    # Time variable to create smooth motion
    t = frame / 30.0
    
    # Update positions of the point lights
    # Simple bowing motion dynamics
    neck_y = np.sin(t) * 0.2  # Neck movement
    head_y = neck_y + 0.5
    pelvis_y = -0.5  # Static pelvis
    
    points_y = [
        head_y,      # Head
        head_y,     # Right shoulder
        head_y,     # Left shoulder
        neck_y,     # Neck
        neck_y - 0.5,  # Upper back
        neck_y - 1.0,  # Lower back
        pelvis_y,   # Pelvis
        pelvis_y - 0.3,  # Right knee
        pelvis_y - 0.3,  # Left knee
        pelvis_y - 0.6,  # Right ankle
        pelvis_y - 0.6,  # Left ankle
    ]
    
    # x positions for corresponding y positions (static horizontal alignment)
    points_x = [0, 0.3, -0.3, 0, 0, 0, 0, 0.2, -0.2, 0, 0]  
    
    # Update point lights
    point_lights.set_data(points_x, points_y)
    return point_lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=60, init_func=init, blit=True, interval=50)

# Display the animation
plt.show()
