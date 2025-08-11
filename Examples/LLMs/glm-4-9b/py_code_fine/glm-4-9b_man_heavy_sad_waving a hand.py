
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

#Parameters for the animation
num_points = 15
total_frames = 200
hand_length = 0.5
hand_wave_amplitude = 0.2
background_color = 'black'

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(8, 6), facecolor=background_color)
ax.set_facecolor(background_color)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Create 15 point lights for the hand
hand_points = [Circle((0.5, 0.5), 0.02, color='white') for _ in range(num_points)]
for point in hand_points:
    ax.add_patch(point)

# Function to update the hand position in each frame
def update(frame):
    angle = 2 * np.pi * frame / total_frames
    hand_wave = hand_wave_amplitude * np.sin(angle)
    
    new_positions = []
    for i in range(num_points):
        point_angle = angle + i * (2 * np.pi / num_points)
        x = 0.5 + hand_length * np.sin(point_angle) * np.sin(angle) + hand_wave * np.cos(point_angle)
        y = 0.5 + hand_length * np.cos(point_angle) * np.sin(angle) - hand_wave * np.sin(point_angle)
        new_positions.append((x, y))
    
    for point, (x, y) in zip(hand_points, new_positions):
        point.center = (x, y)

# Create the animation
animation = FuncAnimation(fig, update, frames=total_frames, interval=50)

# Display the animation
plt.show()
