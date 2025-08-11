
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 200
fps = 30

# Initialize positions
np.random.seed(0)
x = np.zeros(num_lights)
y = np.zeros(num_lights)

# Define joint indices
head = 0
left_shoulder = 1
left_elbow = 2
left_hand = 3
right_shoulder = 4
right_elbow = 5
right_hand = 6
torso_top = 7
torso_bottom = 8
left_hip = 9
left_knee = 10
left_foot = 11
right_hip = 12
right_knee = 13
right_foot = 14

# Initial positions
x[head] = 0
y[head] = 1.5
x[left_shoulder] = -0.5
y[left_shoulder] = 1
x[right_shoulder] = 0.5
y[right_shoulder] = 1
x[torso_top] = 0
y[torso_top] = 0.5
x[torso_bottom] = 0
y[torso_bottom] = -0.5
x[left_hip] = -0.5
y[left_hip] = -1
x[right_hip] = 0.5
y[right_hip] = -1

# Wave motion parameters
wave_amplitude = 0.5
wave_frequency = 0.1

def update(frame):
    # Update head position
    x[head] = np.sin(frame * wave_frequency) * wave_amplitude
    y[head] = 1.5 + np.cos(frame * wave_frequency) * wave_amplitude * 0.2
    
    # Update left arm positions
    x[left_shoulder] = -0.5 + np.sin(frame * wave_frequency) * wave_amplitude * 0.2
    y[left_shoulder] = 1 + np.cos(frame * wave_frequency) * wave_amplitude * 0.1
    x[left_elbow] = x[left_shoulder] - 0.5 + np.sin((frame + 50) * wave_frequency) * wave_amplitude
    y[left_elbow] = y[left_shoulder] - 0.5 + np.cos((frame + 50) * wave_frequency) * wave_amplitude
    x[left_hand] = x[left_elbow] - 0.5 + np.sin((frame + 100) * wave_frequency) * wave_amplitude * 1.5
    y[left_hand] = y[left_elbow] - 0.5 + np.cos((frame + 100) * wave_frequency) * wave_amplitude * 1.5
    
    # Update right arm positions
    x[right_shoulder] = 0.5 + np.sin(frame * wave_frequency) * wave_amplitude * 0.2
    y[right_shoulder] = 1 + np.cos(frame * wave_frequency) * wave_amplitude * 0.1
    x[right_elbow] = x[right_shoulder] + 0.5 + np.sin((frame + 150) * wave_frequency) * wave_amplitude
    y[right_elbow] = y[right_shoulder] - 0.5 + np.cos((frame + 150) * wave_frequency) * wave_amplitude
    x[right_hand] = x[right_elbow] + 0.5 + np.sin((frame + 200) * wave_frequency) * wave_amplitude * 1.5
    y[right_hand] = y[right_elbow] - 0.5 + np.cos((frame + 200) * wave_frequency) * wave_amplitude * 1.5
    
    # Update torso positions
    x[torso_top] = 0
    y[torso_top] = 0.5
    x[torso_bottom] = 0
    y[torso_bottom] = -0.5
    
    # Update leg positions
    x[left_hip] = -0.5
    y[left_hip] = -1
    x[left_knee] = x[left_hip]
    y[left_knee] = y[left_hip] - 1
    x[left_foot] = x[left_knee]
    y[left_foot] = y[left_knee] - 1
    
    x[right_hip] = 0.5
    y[right_hip] = -1
    x[right_knee] = x[right_hip]
    y[right_knee] = y[right_hip] - 1
    x[right_foot] = x[right_knee]
    y[right_foot] = y[right_knee] - 1
    
    scatter.set_offsets(np.c_[x, y])
    return scatter,

# Setup plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 3)
ax.axis('off')
scatter = ax.scatter(x, y, s=100, c='white')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

plt.show()
