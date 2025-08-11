
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Define the number of frames and points
num_frames = 100
num_points = 15

# Define the initial positions of the points (can be adjusted)
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.3, 1.5], # Left Shoulder
    [0.3, 1.5],  # Right Shoulder
    [-0.6, 1.0], # Left Elbow
    [0.6, 1.0],  # Right Elbow
    [-0.9, 0.5], # Left Wrist
    [0.9, 0.5],  # Right Wrist
    [-0.1, 0.8], # Left Hip
    [0.1, 0.8],  # Right Hip
    [-0.4, 0.3], # Left Knee
    [0.4, 0.3],  # Right Knee
    [-0.6, -0.2],# Left Ankle
    [0.6, -0.2], # Right Ankle
    [-0.6, -0.7],# Left Foot
    [0.6, -0.7]  # Right Foot
])

# Scale positions for better visibility
initial_positions *= 2


# Define the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor("black")
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.axis('off')

# Create the scatter plot
scat = ax.scatter([], [], c='white', s=20)

# Function to update the animation
def update(frame):
    # Define movement parameters (adjust to create the desired walking motion)
    phase = frame / num_frames * 2 * np.pi

    # Example motion: simple sinusoidal movement
    x = initial_positions[:, 0].copy()
    y = initial_positions[:, 1].copy()
    
    # Adjust the position to simulate walking motion 
    x[5] += 0.2 * np.sin(phase) # Left wrist
    y[5] -= 0.1 * np.sin(phase)
    x[6] -= 0.2 * np.sin(phase) # Right wrist
    y[6] += 0.1 * np.sin(phase)
    x[11] += 0.3 * np.sin(phase) # Left ankle
    y[11] -= 0.2 * np.sin(phase)
    x[12] -= 0.3 * np.sin(phase) # Right ankle
    y[12] += 0.2 * np.sin(phase)
    x[13] += 0.4 * np.sin(phase) # Left foot
    y[13] -= 0.3 * np.sin(phase)
    x[14] -= 0.4 * np.sin(phase) # Right foot
    y[14] += 0.3 * np.sin(phase)

    x[8] += 0.1 * np.sin(phase)
    y[8] -= 0.05 * np.sin(phase)
    x[7] -= 0.1 * np.sin(phase)
    y[7] += 0.05 * np.sin(phase)


    # Concatenate x and y to form the updated positions
    data = np.stack([x, y], axis=1)
    
    # Update the scatter plot
    scat.set_offsets(data)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Save or show the animation
# ani.save("walking_animation.gif", writer="pillow", fps=30)
plt.show()
