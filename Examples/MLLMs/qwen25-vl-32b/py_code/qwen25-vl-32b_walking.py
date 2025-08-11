
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the point-lights
initial_positions = {
    'head': [0, 1],
    'torso': [0, 0],
    'left_shoulder': [-0.5, 0.5],
    'right_shoulder': [0.5, 0.5],
    'left_elbow': [-1, 0.75],
    'right_elbow': [1, 0.75],
    'left_hand': [-1.5, 0.5],
    'right_hand': [1.5, 0.5],
    'left_hip': [-0.5, -0.5],
    'right_hip': [0.5, -0.5],
    'left_knee': [-1, -1],
    'right_knee': [1, -1],
    'left_foot': [-1.5, -1.5],
    'right_foot': [1.5, -1.5]
}

# Define the amplitude and frequency of the walking cycle
amplitude = 0.5
frequency = 0.05

# Define the function to update the positions of the point-lights
def update_positions(frame):
    positions = initial_positions.copy()
    
    # Update the position of the head
    positions['head'][1] += amplitude * np.sin(frequency * frame)
    
    # Update the position of the torso
    positions['torso'][1] += amplitude * np.sin(frequency * frame)
    
    # Update the position of the left shoulder
    positions['left_shoulder'][1] += amplitude * np.sin(frequency * frame + np.pi / 2)
    
    # Update the position of the right shoulder
    positions['right_shoulder'][1] += amplitude * np.sin(frequency * frame - np.pi / 2)
    
    # Update the position of the left elbow
    positions['left_elbow'][1] += amplitude * np.sin(frequency * frame + np.pi / 2)
    
    # Update the position of the right elbow
    positions['right_elbow'][1] += amplitude * np.sin(frequency * frame - np.pi / 2)
    
    # Update the position of the left hand
    positions['left_hand'][1] += amplitude * np.sin(frequency * frame + np.pi)
    
    # Update the position of the right hand
    positions['right_hand'][1] += amplitude * np.sin(frequency * frame)
    
    # Update the position of the left hip
    positions['left_hip'][1] += amplitude * np.sin(frequency * frame - np.pi / 2)
    
    # Update the position of the right hip
    positions['right_hip'][1] += amplitude * np.sin(frequency * frame + np.pi / 2)
    
    # Update the position of the left knee
    positions['left_knee'][1] += amplitude * np.sin(frequency * frame - np.pi / 2)
    
    # Update the position of the right knee
    positions['right_knee'][1] += amplitude * np.sin(frequency * frame + np.pi / 2)
    
    # Update the position of the left foot
    positions['left_foot'][1] += amplitude * np.sin(frequency * frame)
    
    # Update the position of the right foot
    positions['right_foot'][1] += amplitude * np.sin(frequency * frame + np.pi)
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Create the scatter plot for the point-lights
scatter = ax.scatter([], [], color='white', s=50)

# Define the animation function
def animate(frame):
    positions = update_positions(frame)
    x = [pos[0] for pos in positions.values()]
    y = [pos[1] for pos in positions.values()]
    scatter.set_offsets(np.c_[x, y])
    return scatter,

# Create the animation
animation = FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
