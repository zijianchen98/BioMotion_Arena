
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and frames
num_points = 15
frames = 100

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Create a scatter plot for the points
scat = ax.scatter([], [], color='white', s=5)

# Function to update the position of the points
def update(frame):
    # Define the jumping motion for each point
    t = frame / frames * 2 * np.pi
    positions = np.zeros((num_points, 2))
    
    # Head
    positions[0] = [0.5, 0.7 + 0.1 * np.sin(t)]
    
    # Shoulders
    positions[1] = [0.4, 0.6 + 0.1 * np.sin(t)]
    positions[2] = [0.6, 0.6 + 0.1 * np.sin(t)]
    
    # Elbows
    positions[3] = [0.3, 0.5 + 0.1 * np.sin(t)]
    positions[4] = [0.7, 0.5 + 0.1 * np.sin(t)]
    
    # Hands
    positions[5] = [0.2, 0.4 + 0.1 * np.sin(t)]
    positions[6] = [0.8, 0.4 + 0.1 * np.sin(t)]
    
    # Hips
    positions[7] = [0.4, 0.4 + 0.1 * np.sin(t)]
    positions[8] = [0.6, 0.4 + 0.1 * np.sin(t)]
    
    # Knees
    positions[9] = [0.3, 0.3 + 0.1 * np.sin(t)]
    positions[10] = [0.7, 0.3 + 0.1 * np.sin(t)]
    
    # Feet
    positions[11] = [0.2, 0.2 + 0.1 * np.sin(t)]
    positions[12] = [0.8, 0.2 + 0.1 * np.sin(t)]
    
    # Torso
    positions[13] = [0.5, 0.5 + 0.1 * np.sin(t)]
    positions[14] = [0.5, 0.3 + 0.1 * np.sin(t)]
    
    scat.set_offsets(positions)

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=False)

plt.show()
