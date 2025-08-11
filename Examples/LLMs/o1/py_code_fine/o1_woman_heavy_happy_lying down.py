#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Base positions (15 points) for a "heavy" woman lying down (head on the left, feet on the right)
# Indices:
#  0: Head
#  1: Neck
#  2: Right Shoulder
#  3: Right Elbow
#  4: Right Hand
#  5: Left Shoulder
#  6: Left Elbow
#  7: Left Hand
#  8: Mid Torso
#  9: Right Hip
# 10: Left Hip
# 11: Right Knee
# 12: Left Knee
# 13: Right Foot
# 14: Left Foot

x_base = np.array([
    -2.0, -1.9, -1.8, -1.6, -1.4, 
    -1.8, -1.6, -1.4, -1.5, -1.3, 
    -1.3, -1.0, -1.0, -0.7, -0.7
])

y_base = np.array([
     0.20,  0.20,  0.25,  0.25,  0.25,
     0.15,  0.15,  0.15,  0.00,  0.05,
    -0.05,  0.05, -0.05,  0.05, -0.05
])

fig, ax = plt.subplots(figsize=(8, 4))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim([-2.5, -0.5])
ax.set_ylim([-0.5, 0.5])
ax.axis('off')

# Plot 15 white dots
dots, = ax.plot([], [], 'o', color='white', markersize=6)

def init():
    dots.set_data([], [])
    return [dots]

def animate(frame):
    # Create a smooth, gentle "breathing" motion
    offset = 0.05 * np.sin(frame * 0.1)
    
    # Copy base positions
    x = np.copy(x_base)
    y = np.copy(y_base)
    
    # Shift entire body slightly up/down
    y += offset
    
    # Update dot positions
    dots.set_data(x, y)
    return [dots]

ani = animation.FuncAnimation(
    fig, animate, frames=300, init_func=init, interval=50, blit=True
)

plt.show()