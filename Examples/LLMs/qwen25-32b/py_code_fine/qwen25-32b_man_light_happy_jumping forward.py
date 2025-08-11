
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_points = 15
frames_per_cycle = 60
duration_seconds = 10
fps = 30
total_frames = duration_seconds * fps

# Body part indices
HEAD = 0
SHOULDER_LEFT = 1
SHOULDER_RIGHT = 2
ELBOW_LEFT = 3
ELBOW_RIGHT = 4
HAND_LEFT = 5
HAND_RIGHT = 6
HIP_LEFT = 7
HIP_RIGHT = 8
KNEE_LEFT = 9
KNEE_RIGHT = 10
ANKLE_LEFT = 11
ANKLE_RIGHT = 12
FOOT_LEFT = 13
FOOT_RIGHT = 14

# Initial positions for the point lights
positions = np.zeros((num_points, 2))
positions[HEAD] = [0, 1]
positions[SHOULDER_LEFT] = [-0.2, 0.5]
positions[SHOULDER_RIGHT] = [0.2, 0.5]
positions[ELBOW_LEFT] = [-0.5, 0.3]
positions[ELBOW_RIGHT] = [0.5, 0.3]
positions[HAND_LEFT] = [-0.7, 0.1]
positions[HAND_RIGHT] = [0.7, 0.1]
positions[HIP_LEFT] = [-0.2, -0.5]
positions[HIP_RIGHT] = [0.2, -0.5]
positions[KNEE_LEFT] = [-0.2, -1.0]
positions[KNEE_RIGHT] = [0.2, -1.0]
positions[ANKLE_LEFT] = [-0.2, -1.5]
positions[ANKLE_RIGHT] = [0.2, -1.5]
positions[FOOT_LEFT] = [-0.2, -1.7]
positions[FOOT_RIGHT] = [0.2, -1.7]

# Function to update the position of the points in each frame
def update(frame):
    t = 2 * np.pi * frame / frames_per_cycle
    amplitude = 0.2
    
    # Jumping motion
    y_offset = amplitude * np.sin(t)
    
    # Adjust the positions based on the jump
    positions[:, 1] = [p[1] + y_offset for p in positions]
    
    # Arm swinging motion
    arm_amplitude = 0.2
    arm_t = t + np.pi  # Offset by half cycle for opposite swing
    positions[ELBOW_LEFT][0] = SHOULDER_LEFT[0] - arm_amplitude * np.cos(arm_t)
    positions[HAND_LEFT][0] = ELBOW_LEFT[0] - arm_amplitude * np.cos(arm_t)
    positions[ELBOW_RIGHT][0] = SHOULDER_RIGHT[0] + arm_amplitude * np.cos(arm_t)
    positions[HAND_RIGHT][0] = ELBOW_RIGHT[0] + arm_amplitude * np.cos(arm_t)
    
    # Leg swinging motion
    leg_amplitude = 0.2
    leg_t = t  # Same phase for both legs
    positions[KNEE_LEFT][0] = HIP_LEFT[0] - leg_amplitude * np.cos(leg_t)
    positions[ANKLE_LEFT][0] = KNEE_LEFT[0] - leg_amplitude * np.cos(leg_t)
    positions[KNEE_RIGHT][0] = HIP_RIGHT[0] + leg_amplitude * np.cos(leg_t)
    positions[ANKLE_RIGHT][0] = KNEE_RIGHT[0] + leg_amplitude * np.cos(leg_t)
    
    # Update scatter plot data
    scatter.set_offsets(positions)

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide the axis

# Create scatter plot
scatter = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(total_frames), interval=1000/fps, repeat=True)

plt.show()
