
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the points (a simple standing figure)
# These are just starting points, and will be updated in the animation
points_data = {
    'head': [0, 10],
    'shoulder_l': [-2, 8],
    'shoulder_r': [2, 8],
    'elbow_l': [-4, 5],
    'elbow_r': [4, 5],
    'wrist_l': [-5, 2],
    'wrist_r': [5, 2],
    'hip_l': [-1, 4],
    'hip_r': [1, 4],
    'knee_l': [-2, 1],
    'knee_r': [2, 1],
    'ankle_l': [-2, -2],
    'ankle_r': [2, -2],
    'foot_l': [-3, -4],
    'foot_r': [3, -4]
}

points_labels = list(points_data.keys())
points_pos = np.array(list(points_data.values()))


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background to black
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 12)
ax.set_aspect('equal')
plt.axis('off')  # Hide the axes


# Create the scatter plot
scat = ax.scatter(points_pos[:, 0], points_pos[:, 1], s=50, c='white')  # White points


# Animation function (this is where the motion is defined)
def animate(frame):
    # Example motion: Running with sadman and lightweight features
    # This is a simplified motion model for demonstration
    # You would replace this with more realistic motion data for a
    # true biological motion animation.
    global points_pos

    # Small horizontal movement to simulate running
    horizontal_shift = np.sin(frame * 0.1) * 0.5

    # Arm swinging motion (simplified)
    arm_swing_l = np.sin(frame * 0.2) * 2
    arm_swing_r = -np.sin(frame * 0.2) * 2

    # Leg swinging motion (simplified)
    leg_swing_l = -np.sin(frame * 0.2) * 1.5
    leg_swing_r = np.sin(frame * 0.2) * 1.5

    # Body vertical oscillation (sadman/lightweight feature - small bounce)
    vertical_bounce = np.abs(np.sin(frame * 0.1)) * 0.2
    
    # Update positions
    new_points_pos = points_pos.copy()
    
    new_points_pos[points_labels.index('head'), 1] = points_pos[points_labels.index('head'), 1] + vertical_bounce
    
    new_points_pos[points_labels.index('shoulder_l'), 0] = points_pos[points_labels.index('shoulder_l'), 0] + horizontal_shift
    new_points_pos[points_labels.index('shoulder_r'), 0] = points_pos[points_labels.index('shoulder_r'), 0] + horizontal_shift
    
    new_points_pos[points_labels.index('elbow_l'), 0] = points_pos[points_labels.index('elbow_l'), 0] + horizontal_shift + arm_swing_l
    new_points_pos[points_labels.index('elbow_r'), 0] = points_pos[points_labels.index('elbow_r'), 0] + horizontal_shift + arm_swing_r
    
    new_points_pos[points_labels.index('wrist_l'), 0] = points_pos[points_labels.index('wrist_l'), 0] + horizontal_shift + arm_swing_l * 1.5
    new_points_pos[points_labels.index('wrist_r'), 0] = points_pos[points_labels.index('wrist_r'), 0] + horizontal_shift + arm_swing_r * 1.5

    new_points_pos[points_labels.index('hip_l'), 0] = points_pos[points_labels.index('hip_l'), 0] + horizontal_shift
    new_points_pos[points_labels.index('hip_r'), 0] = points_pos[points_labels.index('hip_r'), 0] + horizontal_shift

    new_points_pos[points_labels.index('knee_l'), 0] = points_pos[points_labels.index('knee_l'), 0] + horizontal_shift + leg_swing_l
    new_points_pos[points_labels.index('knee_r'), 0] = points_pos[points_labels.index('knee_r'), 0] + horizontal_shift + leg_swing_r

    new_points_pos[points_labels.index('ankle_l'), 0] = points_pos[points_labels.index('ankle_l'), 0] + horizontal_shift + leg_swing_l * 1.5
    new_points_pos[points_labels.index('ankle_r'), 0] = points_pos[points_labels.index('ankle_r'), 0] + horizontal_shift + leg_swing_r * 1.5
    
    new_points_pos[points_labels.index('foot_l'), 0] = points_pos[points_labels.index('foot_l'), 0] + horizontal_shift + leg_swing_l * 2
    new_points_pos[points_labels.index('foot_r'), 0] = points_pos[points_labels.index('foot_r'), 0] + horizontal_shift + leg_swing_r * 2


    #Update points_pos so that the whole figure translates across the screen
    total_translation = horizontal_shift/2
    new_points_pos[:,0] = new_points_pos[:,0] + total_translation

    
    scat.set_offsets(new_points_pos)
    points_pos = new_points_pos
    return scat,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, blit=True, repeat=True)

# Save the animation (optional - requires ffmpeg or similar)
# ani.save('running_sadman.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
