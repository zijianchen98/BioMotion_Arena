
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the points (stick figure of a standing person)
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.2, 1.7], # Left Shoulder
    [0.2, 1.7],  # Right Shoulder
    [-0.4, 1.2], # Left Elbow
    [0.4, 1.2],  # Right Elbow
    [-0.6, 0.7], # Left Hand
    [0.6, 0.7],  # Right Hand
    [-0.1, 1.2], # Spine Top
    [0.1, 1.2],  # Spine Top
    [0.0, 0.5],  # Hip Center
    [-0.3, -0.2], # Left Knee
    [0.3, -0.2],  # Right Knee
    [-0.4, -0.9], # Left Foot
    [0.4, -0.9],  # Right Foot
    [0.0, -0.5],  # Lower Spine

])

# Define the sitting animation path function
def sitting_motion(frame_num):
    # Scale down frame number to control speed
    t = frame_num * 0.03

    # Head remains relatively stable
    head_x = initial_positions[0, 0]
    head_y = initial_positions[0, 1] - 0.1 * t

    # Shoulders move down and inwards slightly
    shoulder_x = initial_positions[1:3, 0] * (1 - 0.05 * t)
    shoulder_y = initial_positions[1:3, 1] - 0.2 * t

    # Elbows follow the shoulders and bend slightly
    elbow_x = initial_positions[3:5, 0] * (1 - 0.1 * t)
    elbow_y = initial_positions[3:5, 1] - 0.3 * t

    # Hands move down with elbows
    hand_x = initial_positions[5:7, 0] * (1 - 0.15 * t)
    hand_y = initial_positions[5:7, 1] - 0.4 * t

    # Torso bends
    spine_top_x = initial_positions[7:9, 0] * (1 - 0.05 * t)
    spine_top_y = initial_positions[7:9, 1] - 0.25 * t
    hip_center_x = initial_positions[9, 0] * (1 - 0.1 * t)
    hip_center_y = initial_positions[9, 1] - 0.5 * t
    lower_spine_x = initial_positions[14, 0] * (1 - 0.15 * t)
    lower_spine_y = initial_positions[14, 1] - 0.55 * t

    # Knees bend more significantly
    knee_x = initial_positions[10:12, 0] * (1 - 0.1 * t)
    knee_y = initial_positions[10:12, 1] - 0.7 * t

    # Feet adjust to keep balance
    foot_x = initial_positions[12:14, 0] * (1 - 0.15 * t)
    foot_y = initial_positions[12:14, 1] - 0.75 * t
    
    # Handle the 'sitting' action at frame 30
    if frame_num > 30:
      foot_y = initial_positions[12:14, 1] - 0.75
      knee_y = initial_positions[10:12, 1] - 0.7
      hip_center_y = initial_positions[9, 1] - 0.5
      lower_spine_y = initial_positions[14, 1] - 0.5
      hand_y = initial_positions[5:7, 1] - 0.5
      elbow_y = initial_positions[3:5, 1] - 0.4
      shoulder_y = initial_positions[1:3, 1] - 0.3
      head_y = initial_positions[0, 1] - 0.2

    # Return the updated positions as a single array
    updated_positions = np.array([
        [head_x, head_y],
        [shoulder_x[0], shoulder_y[0]],
        [shoulder_x[1], shoulder_y[1]],
        [elbow_x[0], elbow_y[0]],
        [elbow_x[1], elbow_y[1]],
        [hand_x[0], hand_y[0]],
        [hand_x[1], hand_y[1]],
        [spine_top_x[0], spine_top_y[0]],
        [spine_top_x[1], spine_top_y[1]],
        [hip_center_x, hip_center_y],
        [knee_x[0], knee_y[0]],
        [knee_x[1], knee_y[1]],
        [foot_x[0], foot_y[0]],
        [foot_x[1], foot_y[1]],
        [lower_spine_x, lower_spine_y]
    ])
    return updated_positions


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1.5, 2.5)
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot for the points
scat = ax.scatter([], [], c='white', s=20)

# Initialization function for the animation
def init():
    scat.set_offsets(initial_positions)
    return (scat,)

# Animation function
def animate(frame_num):
    updated_positions = sitting_motion(frame_num)
    scat.set_offsets(updated_positions)
    return (scat,)

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=150, blit=True, repeat=True)

# Display the animation (or save it to a file)
plt.show()

# To save the animation to a file:
# ani.save('sitting_animation.gif', writer='pillow', fps=30)
