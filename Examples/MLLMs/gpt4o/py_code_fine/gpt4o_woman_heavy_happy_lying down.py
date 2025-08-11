
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Function to generate the coordinates for biomechanically plausible motion
def generate_biological_motion(frame):
    # Parameters for animation
    t = frame / 30.0  # time factor to make motion smooth
    
    # Define positions for 15 point-lights representing a lying down human figure
    body_points = np.zeros((15, 2))
    
    # Torso (static)
    body_points[0] = [0.5, 0.8]  # chest
    body_points[1] = [0.5, 0.7]  # mid torso
    body_points[2] = [0.5, 0.6]  # lower torso
    
    # Head (slight motion simulating breathing)
    body_points[3] = [0.5, 0.85 + 0.01 * np.sin(t)]  # head centre
    
    # Arms (simulating relaxation motion)
    body_points[4] = [0.4 + 0.03 * np.sin(t), 0.8]
    body_points[5] = [0.6 - 0.03 * np.sin(t), 0.8]
    body_points[6] = [0.3 + 0.02 * np.sin(t), 0.75]
    body_points[7] = [0.7 - 0.02 * np.sin(t), 0.75]
    
    # Legs (slight bending and weight-shifting motion)
    body_points[8] = [0.45 + 0.02 * np.sin(t), 0.6]
    body_points[9] = [0.55 - 0.02 * np.sin(t), 0.6]
    body_points[10] = [0.42 + 0.015 * np.sin(t), 0.5]
    body_points[11] = [0.58 - 0.015 * np.sin(t), 0.5]
    body_points[12] = [0.40 + 0.01 * np.sin(t), 0.4]
    body_points[13] = [0.60 - 0.01 * np.sin(t), 0.4]
    body_points[14] = [0.5, 0.35]  # ankles (static)
    
    return body_points

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
ax.axis('off')  # Remove axes for clean visuals

# Plot and style the point-lights
points, = ax.plot([], [], 'o', color='white', markersize=8)

# Initialize the animation
def init():
    points.set_data([], [])
    return points,

# Update the animation for each frame
def update(frame):
    positions = generate_biological_motion(frame)
    x, y = positions[:, 0], positions[:, 1]
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=300, init_func=init, blit=True)

# Display the animation
plt.show()
