
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a forward rolling sadman with heavy weight
key_points = [
    "head", "neck", "shoulder_left", "elbow_left", "wrist_left",
    "shoulder_right", "elbow_right", "wrist_right", "hip_left", "knee_left",
    "ankle_left", "hip_right", "knee_right", "ankle_right", "center_of_mass"
]

# Define initial positions of the key points
initial_positions = {
    "head": [0, 1.5],
    "neck": [0, 1.0],
    "shoulder_left": [-0.5, 0.8],
    "elbow_left": [-0.7, 0.5],
    "wrist_left": [-0.9, 0.2],
    "shoulder_right": [0.5, 0.8],
    "elbow_right": [0.7, 0.5],
    "wrist_right": [0.9, 0.2],
    "hip_left": [-0.4, -0.5],
    "knee_left": [-0.6, -1.0],
    "ankle_left": [-0.8, -1.5],
    "hip_right": [0.4, -0.5],
    "knee_right": [0.6, -1.0],
    "ankle_right": [0.8, -1.5],
    "center_of_mass": [0, -0.2]
}

# Define the animation function
def animate(i):
    global positions
    # Update positions based on the forward rolling motion
    angle = i * np.pi / 180  # Convert frame number to angle in radians
    for key in positions:
        x, y = positions[key]
        new_x = x * np.cos(angle) - y * np.sin(angle)
        new_y = x * np.sin(angle) + y * np.cos(angle)
        positions[key] = [new_x, new_y]
    
    # Update the scatter plot data
    x_data = [positions[key][0] for key in key_points]
    y_data = [positions[key][1] for key in key_points]
    sc.set_offsets(np.c_[x_data, y_data])

# Initialize the positions
positions = initial_positions.copy()

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

# Create the scatter plot for the point-lights
sc = ax.scatter([positions[key][0] for key in key_points], 
                [positions[key][1] for key in key_points], 
                color='white', s=10)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=360, interval=20, blit=False)

# Display the animation
plt.show()
