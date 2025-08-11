
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a lying down woman
key_points = [
    (0.2, 0.9),  # Head
    (0.4, 0.85), # Shoulder left
    (0.6, 0.85), # Shoulder right
    (0.3, 0.7),  # Elbow left
    (0.7, 0.7),  # Elbow right
    (0.2, 0.55), # Hand left
    (0.8, 0.55), # Hand right
    (0.4, 0.45), # Hip left
    (0.6, 0.45), # Hip right
    (0.3, 0.3),  # Knee left
    (0.7, 0.3),  # Knee right
    (0.2, 0.15), # Foot left
    (0.8, 0.15), # Foot right
    (0.5, 0.55), # Stomach
    (0.5, 0.35)  # Pelvis
]

# Convert key points to a NumPy array
key_points = np.array(key_points)

# Function to update the frame
def update(frame):
    # Apply a small random perturbation to simulate breathing or slight movement
    perturbation = 0.01 * np.random.randn(*key_points.shape)
    new_positions = key_points + perturbation
    
    # Ensure the points stay within the plot area
    new_positions = np.clip(new_positions, 0, 1)
    
    # Update the scatter plot
    sc.set_offsets(new_positions)
    return sc,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
ax.axis('off')

# Create the scatter plot for the point-lights
sc = ax.scatter(key_points[:, 0], key_points[:, 1], s=50, c='white', edgecolors='none')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=100, blit=True)

# Show the animation
plt.show()
