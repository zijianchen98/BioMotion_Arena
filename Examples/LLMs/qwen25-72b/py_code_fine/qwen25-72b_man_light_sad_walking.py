
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a walking human figure
key_points = [
    'head', 'neck', 'shoulder_left', 'elbow_left', 'wrist_left',
    'shoulder_right', 'elbow_right', 'wrist_right', 'hip_left', 'knee_left',
    'ankle_left', 'hip_right', 'knee_right', 'ankle_right', 'pelvis'
]

# Define the initial positions of the points
initial_positions = {
    'head': [0, 1.8],
    'neck': [0, 1.6],
    'shoulder_left': [-0.3, 1.4],
    'elbow_left': [-0.5, 1.2],
    'wrist_left': [-0.7, 1.0],
    'shoulder_right': [0.3, 1.4],
    'elbow_right': [0.5, 1.2],
    'wrist_right': [0.7, 1.0],
    'hip_left': [-0.2, 0.8],
    'knee_left': [-0.4, 0.6],
    'ankle_left': [-0.6, 0.4],
    'hip_right': [0.2, 0.8],
    'knee_right': [0.4, 0.6],
    'ankle_right': [0.6, 0.4],
    'pelvis': [0, 0.8]
}

# Define the walking motion
def walk(t):
    # Calculate the position of each point at time t
    positions = {point: np.array(initial_positions[point]) for point in key_points}
    
    # Apply a sinusoidal motion to the legs and arms
    leg_angle = np.sin(t) * 0.2
    arm_angle = -np.sin(t) * 0.2
    
    positions['knee_left'] += np.array([-0.2 * np.cos(leg_angle), -0.2 * np.sin(leg_angle)])
    positions['ankle_left'] += np.array([-0.4 * np.cos(leg_angle), -0.4 * np.sin(leg_angle)])
    positions['knee_right'] += np.array([0.2 * np.cos(leg_angle), -0.2 * np.sin(leg_angle)])
    positions['ankle_right'] += np.array([0.4 * np.cos(leg_angle), -0.4 * np.sin(leg_angle)])
    
    positions['elbow_left'] += np.array([-0.2 * np.cos(arm_angle), -0.2 * np.sin(arm_angle)])
    positions['wrist_left'] += np.array([-0.4 * np.cos(arm_angle), -0.4 * np.sin(arm_angle)])
    positions['elbow_right'] += np.array([0.2 * np.cos(arm_angle), -0.2 * np.sin(arm_angle)])
    positions['wrist_right'] += np.array([0.4 * np.cos(arm_angle), -0.4 * np.sin(arm_angle)])
    
    # Shift the entire figure horizontally
    shift = np.sin(t) * 0.2
    for point in positions:
        positions[point][0] += shift
    
    return positions

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-0.5, 2)
ax.set_aspect('equal')
ax.axis('off')
scat = ax.scatter([], [], s=50, color='white')

# Initialize the scatter plot
def init():
    scat.set_offsets([])
    return scat,

# Update the scatter plot for each frame
def update(frame):
    positions = walk(frame)
    points = np.array([positions[point] for point in key_points])
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 120), init_func=init, blit=True)

# Display the animation
plt.show()
