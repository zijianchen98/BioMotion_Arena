
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')

# Number of point lights
num_points = 15

# Initialize the positions of the points
points = np.zeros((num_points, 2))

# Define the initial positions
# Top part of the body (head and upper arm)
points[0] = [0, 0.5]   # Head
points[1] = [-0.5, 0.3] # Left Shoulder
points[2] = [0.5, 0.3]  # Right Shoulder
points[3] = [-0.5, 0.1] # Left Elbow
points[4] = [0.5, 0.1]  # Right Elbow
points[5] = [-0.5, -0.2] # Left Hand
points[6] = [0.5, -0.2]  # Right Hand
points[7] = [0, -0.8]    # Body

# Lower parts (legs)
points[8] = [-0.5, -1.5] # Left Leg
points[9] = [0.5, -1.5]  # Right Leg
points[10] = [-0.2, -1.2] # Left Foot
points[11] = [0.2, -1.2]  # Right Foot
points[12] = [-0.3, -1.3] # Left Foot Bottom
points[13] = [0.3, -1.3]  # Right Foot Bottom
points[14] = [0, -1.0]   # Center of the Body

# Initialize scatter
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

def update(frame):
    # Define waving motion
    wave_amplitude = 0.2 * np.sin(2 * np.pi * frame / 30) # Waving effect
    hand_positions = np.array([
        [0.5, 0.1 + wave_amplitude], # Right Hand
        [0.5, -0.2 + wave_amplitude], # Right Hand Bottom
    ])
    
    points[5:7, :2] = hand_positions  # Update positions of right hand and palm

    scat.set_offsets(points)

    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=60, interval=1000/30, blit=True)

plt.show()
