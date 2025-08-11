
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# parameters
num_points = 15
duration = 10  # seconds
fps = 30
total_frames = duration * fps

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')

# Create a "happyman" lying down (approximated by 15 points)
# Initial positions: head, shoulders, arms, torso, legs
initial_positions = np.array([
    [-2, 1],    # Left shoulder
    [-1, 1.5],  # Left elbow
    [0, 2],     # Left hand
    [1, 1.5],   # Right elbow
    [2, 1],     # Right shoulder
    [0, 0],     # Torso (middle)
    [-1, -1],   # Left hip
    [0, -1.5],  # Groin
    [1, -1],    # Right hip
    [-1.5, -2], # Left knee
    [0, -3],    # Left ankle
    [1.5, -2],  # Right knee
    [0, -3.5],  # Right ankle
    [-2, -1],   # Left foot
    [2, -1]     # Right foot
])

# Create scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=50, c='white')

def update(frame):
    # Calculate time in seconds
    t = frame / fps
    
    # Define the motion trajectories for the body parts
    # Using sinusoidal and circular motion to mimic walking
    def move_head(t):
        offset = 0.2 * np.sin(2 * np.pi * 0.5 * t)
        return np.array([0, 1 + offset])
    
    def move_shoulder(t, side):
        angle = 0.3 * np.sin(2 * np.pi * 0.4 * t)
        radius = 1.5
        if side == 'left':
            return np.array([-2 + radius * np.cos(angle), 1 + radius * np.sin(angle)])
        else:
            return np.array([2 - radius * np.cos(angle), 1 + radius * np.sin(angle)])
    
    def move_arm(t, side):
        angle = 0.5 * np.sin(2 * np.pi * 0.5 * t)
        if side == 'left':
            return np.array([-1 + np.cos(angle), 1.5 + np.sin(angle)])
        else:
            return np.array([1 - np.cos(angle), 1.5 + np.sin(angle)])
    
    def move_hand(t, side):
        angle = 0.7 * np.sin(2 * np.pi * 0.6 * t)
        if side == 'left':
            return np.array([0 + np.cos(angle), 2 + np.sin(angle)])
        else:
            return np.array([0 - np.cos(angle), 2 + np.sin(angle)])
    
    def move_leg(t, side):
        angle = 0.4 * np.sin(2 * np.pi * 0.45 * t)
        if side == 'left':
            return np.array([-1 - np.sin(angle), -1.5 - np.cos(angle)])
        else:
            return np.array([1 + np.sin(angle), -1.5 - np.cos(angle)])
    
    def move_hip(t, side):
        angle = 0.3 * np.sin(2 * np.pi * 0.3 * t)
        if side == 'left':
            return np.array([-1 - 0.5 * np.sin(angle), -1 - 0.5 * np.cos(angle)])
        else:
            return np.array([1 + 0.5 * np.sin(angle), -1 - 0.5 * np.cos(angle)])
    
    def move_knee(t, side):
        angle = 0.5 * np.sin(2 * np.pi * 0.5 * t)
        if side == 'left':
            return np.array([-1.5 - np.sin(angle), -2 - np.cos(angle)])
        else:
            return np.array([1.5 + np.sin(angle), -2 - np.cos(angle)])
    
    def move_ankle(t, side):
        angle = 0.6 * np.sin(2 * np.pi * 0.6 * t)
        if side == 'left':
            return np.array([-2 - np.sin(angle), -3 - np.cos(angle)])
        else:
            return np.array([2 + np.sin(angle), -3 - np.cos(angle)])
    
    # Update positions
    new_positions = np.array([
        move_shoulder(t, 'left'),
        move_arm(t, 'left'),
        move_hand(t, 'left'),
        move_shoulder(t, 'right'),
        move_arm(t, 'right'),
        move_hand(t, 'right'),
        move_head(t),
        move_hip(t, 'left'),
        move_hip(t, 'right'),
        move_knee(t, 'left'),
        move_ankle(t, 'left'),
        move_knee(t, 'right'),
        move_ankle(t, 'right'),
        move_leg(t, 'left'),
        move_leg(t, 'right')
    ])
    
    # Update scatter plot
    scatter.set_offsets(new_positions)
    return scatter,

# Create animation
animation = animation.FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit=True)

# Save animation
animation.save('happyman_llyingdown.mp4', fps=fps, extra_args=['-vcodec', 'libx264'])

# Show animation
plt.show()
