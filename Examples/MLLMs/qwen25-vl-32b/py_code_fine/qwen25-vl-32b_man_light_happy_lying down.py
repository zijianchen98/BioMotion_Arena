
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions represent a person lying down
initial_positions = np.array([
    [0.5, 0.8],  # Head
    [0.4, 0.7],  # Left shoulder
    [0.6, 0.7],  # Right shoulder
    [0.3, 0.6],  # Left elbow
    [0.7, 0.6],  # Right elbow
    [0.2, 0.5],  # Left wrist
    [0.8, 0.5],  # Right wrist
    [0.5, 0.4],  # Pelvis
    [0.4, 0.3],  # Left hip
    [0.6, 0.3],  # Right hip
    [0.3, 0.2],  # Left knee
    [0.7, 0.2],  # Right knee
    [0.2, 0.1],  # Left ankle
    [0.8, 0.1],  # Right ankle
    [0.5, 0.9]   # Tip of the head (optional for balance)
])

# Define the animation frames
num_frames = 100
positions = np.zeros((num_frames, 15, 2))

# Initialize the first frame with the initial positions
positions[0] = initial_positions

# Simulate the lying-down motion
for t in range(1, num_frames):
    # Smooth oscillation for the arms and legs
    arm_amplitude = 0.1 * np.sin(t * 0.1)
    leg_amplitude = 0.1 * np.cos(t * 0.1)
    
    # Update positions
    positions[t] = initial_positions.copy()
    positions[t][2] += arm_amplitude  # Right shoulder
    positions[t][3] += 2 * arm_amplitude  # Right elbow
    positions[t][4] += 3 * arm_amplitude  # Right wrist
    positions[t][5] -= arm_amplitude  # Left shoulder
    positions[t][6] -= 2 * arm_amplitude  # Left elbow
    positions[t][7] -= 3 * arm_amplitude  # Left wrist
    
    positions[t][9] += leg_amplitude  # Right hip
    positions[t][10] += 2 * leg_amplitude  # Right knee
    positions[t][11] += 3 * leg_amplitude  # Right ankle
    positions[t][8] -= leg_amplitude  # Left hip
    positions[t][12] -= 2 * leg_amplitude  # Left knee
    positions[t][13] -= 3 * leg_amplitude  # Left ankle

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide axes
scat = ax.scatter([], [], s=50, c='white')

def update(frame):
    scat.set_offsets(positions[frame])
    return scat,

ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
