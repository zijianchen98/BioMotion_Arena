
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the point lights for the jumping motion
def create_frame(t):
    # Simulated positions of body parts at time 't'
    scale = 0.5
    head = (0, 4 + 0.5 * np.sin(t * np.pi))  # Head bobbles slightly during jump
    shoulders = [(-1, 3), (1, 3)]
    torso = (0, 2 + 0.3 * np.sin(t * np.pi))  # Torso moves slightly with the jump
    hips = [(-1, 1), (1, 1)]
    right_leg = [(-1, 0), (-1, 0 + 0.7 * abs(np.sin(t * np.pi)))]  # Right leg
    left_leg = [(1, 0), (1, 0 + 0.7 * abs(np.sin(t * np.pi)))]  # Left leg
    left_arm = [(-2, 2.7), (-2, 2.7 + 0.5 * np.cos(t * np.pi))]  # Left arm swing motion
    right_arm = [(2, 2.7), (2, 2.7 - 0.5 * np.cos(t * np.pi))]  # Right arm swing motion
    
    # Combine into a single list for plotting
    points = [head] + shoulders + [torso] + hips + right_leg + left_leg + left_arm + right_arm
    scaled_points = [(x * scale, y * scale) for x, y in points]  # Optional: scale to fit screen
    return zip(*scaled_points)

# Animate the point-light stimulus
def animate(i):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 5)
    ax.axis('off')  # Hide axes
    
    x, y = create_frame(i * 0.1)
    ax.scatter(x, y, c='white', s=50)  # Draw white points against black background

# Create the plot
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()
