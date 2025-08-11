
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for a walking person
def walking_points(t):
    # Define the points for the head, torso, arms, and legs
    head = np.array([0, 0.5])
    torso = np.array([0, 0.2])
    arm1 = np.array([0.1 * np.sin(2 * t), 0.1 * np.cos(2 * t) + 0.2])
    arm2 = np.array([-0.1 * np.sin(2 * t), 0.1 * np.cos(2 * t) + 0.2])
    hand1 = np.array([0.2 * np.sin(2 * t), 0.2 * np.cos(2 * t) + 0.2])
    hand2 = np.array([-0.2 * np.sin(2 * t), 0.2 * np.cos(2 * t) + 0.2])
    leg1 = np.array([0.1 * np.sin(t), -0.3 * np.cos(t) - 0.2])
    leg2 = np.array([-0.1 * np.sin(t), -0.3 * np.cos(t) - 0.2])
    foot1 = np.array([0.2 * np.sin(t), -0.5 * np.cos(t) - 0.2])
    foot2 = np.array([-0.2 * np.sin(t), -0.5 * np.cos(t) - 0.2])
    shoulder1 = np.array([0.05 * np.sin(2 * t), 0.05 * np.cos(2 * t) + 0.2])
    shoulder2 = np.array([-0.05 * np.sin(2 * t), 0.05 * np.cos(2 * t) + 0.2])
    hip1 = np.array([0.05 * np.sin(t), -0.1 * np.cos(t) - 0.2])
    hip2 = np.array([-0.05 * np.sin(t), -0.1 * np.cos(t) - 0.2])
    knee1 = np.array([0.1 * np.sin(t), -0.2 * np.cos(t) - 0.2])
    knee2 = np.array([-0.1 * np.sin(t), -0.2 * np.cos(t) - 0.2])
    
    # Combine the points into a single array
    points = np.array([
        head, torso, arm1, arm2, hand1, hand2, leg1, leg2, foot1, foot2,
        shoulder1, shoulder2, hip1, hip2, knee1, knee2
    ])
    
    return points

# Create a new figure
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_axis_off()

# Initialize the plot with the initial points
points = walking_points(0)
scatter = ax.scatter(points[:, 0], points[:, 1], s=50, c='w')

# Animation function
def animate(t):
    points = walking_points(t)
    scatter.set_offsets(points)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 2 * np.pi, 128), blit=True)

plt.show()
