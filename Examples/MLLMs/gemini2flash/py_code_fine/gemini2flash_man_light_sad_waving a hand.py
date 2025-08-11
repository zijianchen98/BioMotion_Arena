
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the points
# These are just initial guesses, and the animation logic will move them
points_data = {
    'head': [0, 1.8],
    'shoulder_l': [-0.5, 1.5],
    'shoulder_r': [0.5, 1.5],
    'elbow_l': [-1.0, 1.0],
    'elbow_r': [1.0, 1.0],
    'wrist_l': [-1.5, 0.5],
    'wrist_r': [1.5, 0.5],
    'hip_l': [-0.3, 0.5],
    'hip_r': [0.3, 0.5],
    'knee_l': [-0.3, 0.0],
    'knee_r': [0.3, 0.0],
    'ankle_l': [-0.3, -0.5],
    'ankle_r': [0.3, -0.5],
    'torso': [0, 1.0],
    'waist': [0, 0.5]
}

points_list = list(points_data.values())
points = np.array(points_list)

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-3, 3)
ax.set_ylim(-2, 3)
ax.set_aspect('equal')
plt.axis('off')


# Create the scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Define the animation function
def animate(i):
    # Update the positions of the points to simulate waving
    # This is a simplified example, you'll likely need more complex logic
    # to create realistic motion
    global points
    
    # Example: waving right hand
    wave_amplitude = np.sin(i * 0.1) * 0.5  # Amplitude of the wave
    points[6, 0] = 1.5 + wave_amplitude  # Move right wrist horizontally
    points[6, 1] = 0.5 + np.cos(i * 0.1) * 0.2 #Move right wrist vertically


    # Slightly move the entire body to mimic natural sway
    body_sway = np.sin(i * 0.05) * 0.05
    points[:, 0] += body_sway
    
    # Torso and waist slightly move vertically as well
    points[13, 1] += np.cos(i * 0.05) * 0.02  # Torso
    points[14, 1] += np.sin(i * 0.05) * 0.02  # Waist
    
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, blit=True, repeat=True)

# Show the animation
plt.show()
