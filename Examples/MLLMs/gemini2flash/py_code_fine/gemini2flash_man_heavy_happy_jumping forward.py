
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_points = 15

# Define the animation parameters
duration = 5  # Duration of the animation in seconds
fps = 30  # Frames per second
num_frames = duration * fps

# Define the initial positions of the point lights
# Adjust these values to match the example image
initial_positions = np.array([
    [0.0, 3.0],    # Head
    [-0.5, 2.5],   # Left Shoulder
    [0.5, 2.5],    # Right Shoulder
    [-0.75, 2.0],  # Left Elbow
    [0.75, 2.0],   # Right Elbow
    [-1.0, 1.5],   # Left Wrist
    [1.0, 1.5],    # Right Wrist
    [-0.25, 1.25],  # Torso 1
    [0.25, 1.25],   # Torso 2
    [0.0, 1.0],    # Torso 3
    [-0.25, 0.5],   # Hip Left
    [0.25, 0.5],    # Hip Right
    [-0.25, 0.0],  # Knee Left
    [0.25, 0.0],   # Knee Right
    [0.0, -0.5]     # Ankle
])

# Scale the positions
initial_positions *= 2

# Define the motion of the point lights for a jumping forward action
def generate_motion(num_frames):
    motion = np.zeros((num_frames, num_points, 2))
    for i in range(num_points):
        # Define general movement for all joints (forward jump)
        motion[:, i, 1] = np.sin(np.linspace(0, 2 * np.pi, num_frames)) * 0.2
        motion[:, i, 0] = np.linspace(0, 1.0, num_frames)
        
    # Modify specific joints to simulate jumping action
    # Arms swing forward
    motion[:, 3, 1] += np.sin(np.linspace(0, 4 * np.pi, num_frames)) * 0.3
    motion[:, 4, 1] += np.sin(np.linspace(0, 4 * np.pi, num_frames)) * 0.3
    # Knees bend and extend
    motion[:, 12, 1] -= np.sin(np.linspace(0, 4 * np.pi, num_frames)) * 0.4
    motion[:, 13, 1] -= np.sin(np.linspace(0, 4 * np.pi, num_frames)) * 0.4
    return motion

motion = generate_motion(num_frames)

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-5, 6)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
plt.axis('off')  # Hide the axes

# Create the scatter plot for the point lights
scat = ax.scatter([], [], s=50, c='white')

# Define the animation function
def animate(frame):
    positions = initial_positions + motion[frame]
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True)

# Save the animation (optional)
#ani.save('jumping_motion.mp4', fps=fps)

# Display the animation
plt.show()
