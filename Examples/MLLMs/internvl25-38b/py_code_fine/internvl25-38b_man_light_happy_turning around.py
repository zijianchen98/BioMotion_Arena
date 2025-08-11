
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to update the position of the points
def update(frame, points, ax, interval):
    # Convert frame to time in seconds
    t = frame * interval / 1000.0
    
    # Define the motion for a turning around action
    phase = 2 * np.pi * t  # Phase of the rotation
    for i, pt in enumerate(points):
        angle = np.pi / 2 - phase  # Starting angle
        if i <= 5:  # Head and upper body
            radius = 0.5 + 0.1 * np.sin(2 * phase)
            x = np.sin(angle) * radius
            y = np.cos(angle) * radius
        elif i <= 10:  # Arms
            radius = 1.0
            arm_phase = phase + (i - 6) * np.pi / 6
            x = np.sin(angle - arm_phase) * radius
            y = np.cos(angle - arm_phase) * radius
        else:  # Legs
            radius = 1.0
            leg_phase = phase + (i - 11) * np.pi / 6
            x = np.sin(angle - leg_phase) * radius
            y = np.cos(angle - leg_phase) * radius
        
        pt.set_data([x], [y])
    
    return points

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')

# Create 15 point-lights
points = [ax.plot([], [], 'wo', ms=10)[0] for _ in range(15)]

# Animation setup
interval = 50  # milliseconds
ani = animation.FuncAnimation(fig, update, frames=range(0, 100), fargs=(points, ax, interval), interval=interval, blit=True)

plt.show()
