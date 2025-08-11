
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of lights
num_lights = 15

# Define initial positions of the lights (simplified for lying down position)
positions = np.array([
    [0.5, 0.4], [0.4, 0.3], [0.6, 0.3], # head
    [0.3, 0.5], [0.7, 0.5],             # shoulders
    [0.2, 0.6], [0.8, 0.6],             # elbows
    [0.1, 0.7], [0.9, 0.7],             # wrists
    [0.4, 0.7], [0.6, 0.7],             # hips
    [0.2, 0.8], [0.8, 0.8],             # knees
    [0.1, 0.9], [0.9, 0.9]              # ankles
])

# Define the amplitude and frequency of the oscillations
amplitude = 0.05
frequency = 0.1

def update(frame):
    global positions
    # Update the positions based on sine waves for a lying down motion
    for i in range(num_lights):
        if i < 3:  # head nodding motion
            positions[i][1] += amplitude * np.sin(frequency * frame)
        elif 2 < i < 5:  # shoulder heaving motion
            positions[i][1] += amplitude * np.sin(frequency * frame + np.pi / 2)
        elif 4 < i < 7:  # arm swinging motion
            positions[i][0] += amplitude * np.cos(frequency * frame)
        elif 6 < i < 9:  # hand flicking motion
            positions[i][0] += amplitude * np.sin(frequency * frame)
        elif 8 < i < 11:  # hip rolling motion
            positions[i][0] += amplitude * np.sin(frequency * frame)
        elif 10 < i < 13:  # knee bending motion
            positions[i][1] -= amplitude * np.sin(frequency * frame)
        else:  # ankle twitching motion
            positions[i][1] -= amplitude * np.sin(frequency * frame + np.pi / 2)

    # Clear the current plot and redraw points
    plt.cla()
    plt.scatter(positions[:, 0], positions[:, 1], color='white', s=100)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_facecolor('black')
    plt.axis('off')

fig = plt.figure(figsize=(5, 5))
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)
plt.show()
