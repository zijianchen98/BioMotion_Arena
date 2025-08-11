
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 50

# Define the number of points
num_points = 15

# Define the initial positions of the points to form a jumping stick figure
initial_positions = np.array([
    [0, 5],       # Head
    [-1, 4],      # Left shoulder
    [1, 4],       # Right shoulder
    [-2, 3],      # Left elbow
    [2, 3],       # Right elbow
    [-3, 2],      # Left wrist
    [3, 2],       # Right wrist
    [-0.5, 3],    # Torso
    [-1, 1],      # Left hip
    [1, 1],       # Right hip
    [-2, 0],      # Left knee
    [2, 0],       # Right knee
    [-3, -1],     # Left ankle
    [3, -1],     # Right ankle
    [0,2] #abdomen
])

# Define the motion of the points to simulate jumping, keeping it relatively simple
motion = np.zeros((num_frames, num_points, 2))
for i in range(num_points):
    motion[:, i, 1] = np.sin(np.linspace(0, 4 * np.pi, num_frames)) * 0.5  # Vertical movement for jumping
    motion[:, i, 0] = np.sin(np.linspace(0, 2 * np.pi, num_frames)) * 0.2  # Slight horizontal sway

# Adjust specific points to simulate leg and arm movements during a jump
# Adjust left knee and ankle
motion[:, 10, 0] += np.sin(np.linspace(0, 6 * np.pi, num_frames)) * 0.4 #horizontal left knee
motion[:, 12, 0] += np.sin(np.linspace(0, 6 * np.pi, num_frames)) * 0.5 #horizontal left ankle

#Adjust right knee and ankle
motion[:, 11, 0] -= np.sin(np.linspace(0, 6 * np.pi, num_frames)) * 0.4  #horizontal right knee
motion[:, 13, 0] -= np.sin(np.linspace(0, 6 * np.pi, num_frames)) * 0.5  #horizontal right ankle

#Adjust shoulders
motion[:, 1, 0] -= np.sin(np.linspace(0, 2 * np.pi, num_frames)) * 0.1 #horizontal left shoulder
motion[:, 2, 0] += np.sin(np.linspace(0, 2 * np.pi, num_frames)) * 0.1 #horizontal right shoulder


# Add the motion to the initial positions
positions = initial_positions + motion

# Scale positions for better visualization
positions *= 10

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background to black
ax.set_xlim(-40, 40)
ax.set_ylim(-30, 60)
ax.set_aspect('equal')
plt.axis('off')  # Hide the axes

# Create the scatter plot for the points
scatter = ax.scatter(positions[0, :, 0], positions[0, :, 1], color='white', s=50)  # White points

# Animation function
def animate(i):
    scatter.set_offsets(positions[i, :, :])
    return (scatter,)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
