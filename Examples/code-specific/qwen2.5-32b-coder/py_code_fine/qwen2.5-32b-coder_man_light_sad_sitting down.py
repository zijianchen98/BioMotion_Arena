
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights and the frames per second
num_lights = 15
fps = 30
duration = 5  # seconds
frames = int(fps * duration)

# Initialize positions of the point lights (15 points)
# These positions are placeholders and need to be refined for a more accurate representation
initial_positions = np.array([
    [0.0, 0.8],  # Head
    [-0.1, 0.7], # Left Eye
    [0.1, 0.7],  # Right Eye
    [0.0, 0.6],  # Nose
    [0.0, 0.5],  # Mouth
    [-0.1, 0.4], # Left Shoulder
    [0.1, 0.4],  # Right Shoulder
    [-0.2, 0.2], # Left Elbow
    [0.2, 0.2],  # Right Elbow
    [-0.2, 0.0], # Left Hand
    [0.2, 0.0],  # Right Hand
    [0.0, 0.3],  # Chest
    [0.0, 0.1],  # Waist
    [-0.1, -0.1],# Left Hip
    [0.1, -0.1]  # Right Hip
])

# Function to generate a smooth sitting down motion
def generate_motion(t):
    # t ranges from 0 to 1 over the duration of the animation
    head = np.array([0.0, 0.8 - 0.2 * t])
    eyes = np.array([[-0.1, 0.7 - 0.1 * t], [0.1, 0.7 - 0.1 * t]])
    nose = np.array([0.0, 0.6 - 0.1 * t])
    mouth = np.array([0.0, 0.5 - 0.1 * t])
    shoulders = np.array([[-0.1, 0.4 - 0.1 * t], [0.1, 0.4 - 0.1 * t]])
    elbows = np.array([[-0.2, 0.2 - 0.2 * t], [0.2, 0.2 - 0.2 * t]])
    hands = np.array([[-0.2, 0.0 - 0.2 * t], [0.2, 0.0 - 0.2 * t]])
    chest = np.array([0.0, 0.3 - 0.1 * t])
    waist = np.array([0.0, 0.1 - 0.2 * t])
    hips = np.array([[-0.1, -0.1 - 0.2 * t], [0.1, -0.1 - 0.2 * t]])
    
    return np.vstack((head, eyes, nose, mouth, shoulders, elbows, hands, chest, waist, hips))

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create scatter plot for point lights
scatter = ax.scatter([], [], s=100, color='white')

# Initialization function
def init():
    scatter.set_offsets([])
    return scatter,

# Animation function
def animate(i):
    t = i / frames
    positions = generate_motion(t)
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=1000/fps, blit=True)

# Show the animation
plt.show()
