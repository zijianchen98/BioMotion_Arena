
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def generate_laying_down_motion(t):
    # Coordinates for a person lying down with 15 white point lights
    # Each light represents a joint or main feature of the body
    
    # Base positions
    head_x, head_y = 0, 10
    torso_x, torso_y = 0, 8
    left_shoulder_x, left_shoulder_y = -2, 8
    right_shoulder_x, right_shoulder_y = 2, 8
    left_elbow_x, left_elbow_y = -3, 7
    right_elbow_x, right_elbow_y = 3, 7
    left_hand_x, left_hand_y = -3.5, 6.5
    right_hand_x, right_hand_y = 3.5, 6.5
    left_hip_x, left_hip_y = -1, 6
    right_hip_x, right_hip_y = 1, 6
    left_knee_x, left_knee_y = -1.5, 4.5
    right_knee_x, right_knee_y = 1.5, 4.5
    left_foot_x, left_foot_y = -2, 3
    right_foot_x, right_foot_y = 2, 3

    # Simple oscillatory motion for limbs
    elbow_movement = np.sin(t) * 0.5
    knee_movement = np.sin(t) * 0.7
    foot_movement = np.sin(t) * 0.6

    # Update positions for biomechanical motion
    left_elbow_y += elbow_movement
    right_elbow_y += elbow_movement
    left_knee_y += knee_movement
    right_knee_y += knee_movement
    left_foot_y += foot_movement
    right_foot_y += foot_movement
    left_hand_y -= elbow_movement / 2
    right_hand_y -= elbow_movement / 2

    # Return positions as an array
    return np.array([
        [head_x, head_y],
        [torso_x, torso_y],
        [left_shoulder_x, left_shoulder_y],
        [right_shoulder_x, right_shoulder_y],
        [left_elbow_x, left_elbow_y],
        [right_elbow_x, right_elbow_y],
        [left_hand_x, left_hand_y],
        [right_hand_x, right_hand_y],
        [left_hip_x, left_hip_y],
        [right_hip_x, right_hip_y],
        [left_knee_x, left_knee_y],
        [right_knee_x, right_knee_y],
        [left_foot_x, left_foot_y],
        [right_foot_x, right_foot_y]
    ])

def animate(frame, scat):
    t = frame / 10.0
    positions = generate_laying_down_motion(t)
    scat.set_offsets(positions)
    return scat,

# Initialize the plot
fig, ax = plt.subplots()
fig.set_size_inches(6, 6)
ax.set_xlim(-4, 4)
ax.set_ylim(0, 12)
ax.set_facecolor('black')

# Create the scatter plot for the point lights
positions = generate_laying_down_motion(0)
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Set up animation
ani = animation.FuncAnimation(fig, animate, frames=200, fargs=(scat,), interval=50, blit=True)

# Display the animation
plt.show()
