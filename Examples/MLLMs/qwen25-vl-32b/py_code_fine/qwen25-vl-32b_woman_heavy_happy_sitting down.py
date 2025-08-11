
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These points represent: Head, Shoulders, Elbows, Wrists, Hips, Knees, Ankles
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], # Left Shoulder
    [1, -1],  # Right Shoulder
    [-2, -3], # Left Elbow
    [2, -3],  # Right Elbow
    [-1, -4], # Left Wrist
    [1, -4],  # Right Wrist
    [0, -2],  # Hip
    [-1, -4], # Left Knee
    [1, -4],  # Right Knee
    [-1, -6], # Left Ankle
    [1, -6],  # Right Ankle
])

# Define the trajectory for sitting down
def sitting_down_animation(t):
    """
    Simulate the motion of a woman sitting down.
    t: Time parameter (0 to 1)
    """
    # Smooth transition using a sine wave for natural motion
    progress = np.sin(t * np.pi / 2)  # Sine wave from 0 to 1
    
    # Update positions based on the progress
    positions = initial_positions.copy()
    
    # Move the head slightly forward and downward
    positions[0] += np.array([0, -progress])
    
    # Move the shoulders downward
    positions[1:3] += np.array([0, -progress * 2])
    
    # Move the elbows and wrists downward
    positions[3:7] += np.array([0, -progress * 3])
    
    # Move the hips downward and slightly forward
    positions[7] += np.array([-progress * 0.5, -progress * 4])
    
    # Move the knees and ankles downward
    positions[8:12] += np.array([0, -progress * 5])
    
    # Adjust the left and right sides symmetrically
    positions[1:3] *= (1 - progress * 0.2)  # Slight inward movement of shoulders
    positions[3:7] *= (1 - progress * 0.3)  # Slight inward movement of arms
    positions[8:12] *= (1 - progress * 0.2)  # Slight inward movement of legs
    
    return positions

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-7, 1)
ax.axis('off')  # Hide axes for a clean background

# Scatter plot for the point-lights
scatter = ax.scatter([], [], s=50, c='white')

def update(frame):
    """Update function for the animation."""
    positions = sitting_down_animation(frame / 50)  # Normalize frame to [0, 1]
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=50, interval=50, blit=True
)

# Display the animation
plt.show()
