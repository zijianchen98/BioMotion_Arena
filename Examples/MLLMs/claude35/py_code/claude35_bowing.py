
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create the positions of the point lights
def get_bow_motion(frame):
    # Define parameters for bowing motion
    neck_y = 2.5 * np.sin(np.radians(frame * 3))
    torso_y = 2.0 * np.sin(np.radians(frame * 3))
    
    # Define the heights of each joint point
    positions = np.array([
        [0, neck_y],    # Head
        [0, neck_y - 0.5],  # Neck
        [0, torso_y - 1],   # Torso
        [-0.5, torso_y - 1.5],  # Left shoulder
        [0.5, torso_y - 1.5],  # Right shoulder
        [-0.5, torso_y - 2],  # Left elbow
        [0.5, torso_y - 2],  # Right elbow
        [-0.5, torso_y - 2.5],  # Left wrist
        [0.5, torso_y - 2.5],  # Right wrist
        [-0.5, torso_y - 3],  # Left hip
        [0.5, torso_y - 3],  # Right hip
        [-0.5, torso_y - 3.5],  # Left knee
        [0.5, torso_y - 3.5],  # Right knee
        [-0.5, torso_y - 4],  # Left ankle
        [0.5, torso_y - 4]   # Right ankle
    ])
    
    return positions

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-5, 1)
ax.set_facecolor('black')
ax.axis('off')  # Hide axes

# Create line objects for the point lights
points = [ax.plot([], [], 'o', color='white')[0] for _ in range(15)]

# Animation function
def animate(frame):
    positions = get_bow_motion(frame)
    for point, pos in zip(points, positions):
        point.set_data(pos[0], pos[1])
    return points

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 60, 0.5), blit=True)

# Display the animation
plt.show()
