
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Number of point lights
num_points = 15

# Initial positions of point lights - simplified human body representation
points = {
    'head': (5, 9),
    'shoulder_left': (4.5, 8),
    'shoulder_right': (5.5, 8),
    'elbow_left': (4.5, 6),
    'elbow_right': (5.5, 6),
    'wrist_left': (4.5, 5),
    'wrist_right': (5.5, 5),
    'hip_left': (4, 7),
    'hip_right': (6, 7),
    'knee_left': (4, 4),
    'knee_right': (6, 4),
    'ankle_left': (4, 2),
    'ankle_right': (6, 2),
    'foot_left': (3.5, 1),
    'foot_right': (6.5, 1),
}

# Define the initial scatter plot
scat = ax.scatter([], [], color='white', s=100)

# Animation update function
def update(frame):
    # Define the waving motion for the arms
    wave_amplitude = 0.5
    wave_frequency = 0.15
    right_wrist_y = 5 + wave_amplitude * np.sin(wave_frequency * frame)
    left_wrist_y = 5 - wave_amplitude * np.sin(wave_frequency * frame)
    
    # Update the positions of the points
    points['wrist_right'] = (5.5, right_wrist_y)
    points['wrist_left'] = (4.5, left_wrist_y)
    
    # Flatten the points for scatter
    x_data = [p[0] for p in points.values()]
    y_data = [p[1] for p in points.values()]
    
    # Update scatter plot data
    scat.set_offsets(np.c_[x_data, y_data])
    
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50, blit=True)

# Show the animation
plt.show()
