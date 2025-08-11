
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights and their initial positions
lights = np.array([
    [0, 0],  # Head
    [-0.1, 0.1], [0.1, 0.1],  # Shoulders
    [-0.2, 0.2], [0.2, 0.2],  # Elbows
    [-0.3, 0.3], [0.3, 0.3],  # Hands
    [0, -0.1],  # Hips
    [-0.1, -0.2], [0.1, -0.2],  # Knees
    [-0.2, -0.3], [0.2, -0.3],  # Ankles
    [-0.15, 0.05], [0.15, 0.05],  # Torso
    [-0.1, -0.05], [0.1, -0.05],  # Upper body
])

# Define the movement of the point-lights
def animate(frame):
    angle = np.radians(frame)
    bow_angle = np.radians(30 * np.sin(np.radians(frame)))
    
    # Move the head
    lights[0] = [0, 0.1 * np.sin(angle)]
    
    # Move the shoulders
    lights[1] = [-0.1 * np.cos(angle), 0.1 * np.sin(angle)]
    lights[2] = [0.1 * np.cos(angle), 0.1 * np.sin(angle)]
    
    # Move the elbows
    lights[3] = [-0.2 * np.cos(angle + bow_angle), 0.2 * np.sin(angle + bow_angle)]
    lights[4] = [0.2 * np.cos(angle + bow_angle), 0.2 * np.sin(angle + bow_angle)]
    
    # Move the hands
    lights[5] = [-0.3 * np.cos(angle + 2 * bow_angle), 0.3 * np.sin(angle + 2 * bow_angle)]
    lights[6] = [0.3 * np.cos(angle + 2 * bow_angle), 0.3 * np.sin(angle + 2 * bow_angle)]
    
    # Move the hips
    lights[7] = [0, -0.1 * np.sin(angle)]
    
    # Move the knees
    lights[8] = [-0.1 * np.cos(angle - bow_angle), -0.2 * np.sin(angle - bow_angle)]
    lights[9] = [0.1 * np.cos(angle - bow_angle), -0.2 * np.sin(angle - bow_angle)]
    
    # Move the ankles
    lights[10] = [-0.2 * np.cos(angle - 2 * bow_angle), -0.3 * np.sin(angle - 2 * bow_angle)]
    lights[11] = [0.2 * np.cos(angle - 2 * bow_angle), -0.3 * np.sin(angle - 2 * bow_angle)]
    
    # Move the torso
    lights[12] = [-0.15 * np.cos(angle), 0.05 * np.sin(angle)]
    lights[13] = [0.15 * np.cos(angle), 0.05 * np.sin(angle)]
    
    # Move the upper body
    lights[14] = [-0.1 * np.cos(angle - bow_angle), -0.05 * np.sin(angle - bow_angle)]
    lights[15] = [0.1 * np.cos(angle - bow_angle), -0.05 * np.sin(angle - bow_angle)]
    
    return lights

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-0.4, 0.4)
ax.set_ylim(-0.4, 0.4)
ax.set_aspect('equal')
ax.set_facecolor('black')

scatter = ax.scatter(lights[:, 0], lights[:, 1], color='white')

def update(frame):
    new_positions = animate(frame)
    scatter.set_offsets(new_positions)
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=range(0, 360), interval=20)

plt.show()
