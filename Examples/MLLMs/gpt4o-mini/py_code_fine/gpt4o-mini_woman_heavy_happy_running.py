
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point-lights
num_points = 15

# Initialize positions of the point-lights (15 points)
# For example, simple running posture points as a placeholder
points = np.array([
    [0, 2],  # Head
    [-0.5, 1.5], [0.5, 1.5],  # Shoulders
    [-0.8, 1], [0.8, 1],  # Elbows
    [-1.0, 0.5], [0.0, 0.5], [1.0, 0.5],  # Hands
    [-0.5, 0], [0.5, 0],  # Body
    [-0.5, -1], [0.5, -1],  # Knees
    [-0.2, -2], [0.2, -2],  # Feet
    [0, -3]  # Center of weight
])

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 3)
ax.set_facecolor('black')
points_plot = [plt.plot([], [], 'o', color='white')[0] for _ in range(num_points)]

def update(frame):
    # Update positions for a running motion
    # Simple running-like motion (you can adjust the cycle for realism)
    time = frame / 10.0  # Modify speed
    vertical_shift = 0.5 * np.sin(time)  # Vertical oscillation
    horizontal_shift = 0.1 * frame  # Forward motion

    updated_positions = points + np.array([[horizontal_shift, vertical_shift]] * num_points)
    
    for i, pt in enumerate(updated_positions):
        points_plot[i].set_data(pt[0], pt[1])
    
    return points_plot

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), blit=True, interval=50)

plt.show()
