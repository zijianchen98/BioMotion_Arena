
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These points represent the head, shoulders, elbows, wrists, hips, knees, and ankles
initial_positions = np.array([
    [0.5, 1.0],  # Head
    [0.4, 0.8],  # Left shoulder
    [0.6, 0.8],  # Right shoulder
    [0.3, 0.5],  # Left elbow
    [0.7, 0.5],  # Right elbow
    [0.4, 0.3],  # Left wrist
    [0.6, 0.3],  # Right wrist
    [0.5, 0.6],  # Hips
    [0.4, 0.4],  # Left knee
    [0.6, 0.4],  # Right knee
    [0.3, 0.2],  # Left ankle
    [0.7, 0.2],  # Right ankle
])

# Define the trajectory for sitting down
def sitting_down(t):
    """
    Simulate the motion of sitting down.
    t: Time parameter (0 to 1)
    """
    # Smooth transition using a cubic easing function
    ease_in_out = 3 * t**2 - 2 * t**3
    
    # Define the movement for each body part
    positions = initial_positions.copy()
    
    # Head: Slightly move downward and forward
    positions[0] = [0.5 + 0.05 * ease_in_out, 1.0 - 0.2 * ease_in_out]
    
    # Shoulders: Move downward
    positions[1] = [0.4, 0.8 - 0.2 * ease_in_out]
    positions[2] = [0.6, 0.8 - 0.2 * ease_in_out]
    
    # Elbows: Move downward and slightly outward
    positions[3] = [0.3 - 0.05 * ease_in_out, 0.5 - 0.1 * ease_in_out]
    positions[4] = [0.7 + 0.05 * ease_in_out, 0.5 - 0.1 * ease_in_out]
    
    # Wrists: Move downward and outward
    positions[5] = [0.4 - 0.1 * ease_in_out, 0.3 - 0.2 * ease_in_out]
    positions[6] = [0.6 + 0.1 * ease_in_out, 0.3 - 0.2 * ease_in_out]
    
    # Hips: Move downward
    positions[7] = [0.5, 0.6 - 0.3 * ease_in_out]
    
    # Knees: Move downward and inward
    positions[8] = [0.4 - 0.1 * ease_in_out, 0.4 - 0.3 * ease_in_out]
    positions[9] = [0.6 + 0.1 * ease_in_out, 0.4 - 0.3 * ease_in_out]
    
    # Ankles: Move downward
    positions[10] = [0.3, 0.2 - 0.2 * ease_in_out]
    positions[11] = [0.7, 0.2 - 0.2 * ease_in_out]
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide axes for a cleaner look
scat = ax.scatter([], [], s=50, c='white')

# Animation function
def update(frame):
    t = frame / 50.0  # Normalize time (0 to 1 over 50 frames)
    positions = sitting_down(t)
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=50, interval=50, blit=True)

# Display the animation
plt.show()
