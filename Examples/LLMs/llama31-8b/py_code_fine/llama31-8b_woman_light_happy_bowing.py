
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters of the animation
num_points = 15
background_color = 'black'
point_color = 'white'
num_frames = 100
frame_rate = 30

# Define the points that make up the happy woman
points = np.array([
    [0, 0],  # Head
    [0, -0.2],  # Left ear
    [0, 0.2],  # Right ear
    [-0.2, -0.1],  # Left shoulder
    [-0.2, 0.1],  # Right shoulder
    [0.2, -0.1],  # Left hip
    [0.2, 0.1],  # Right hip
    [-0.1, 0.3],  # Left elbow
    [-0.1, -0.3],  # Right elbow
    [0.1, 0.3],  # Left wrist
    [0.1, -0.3],  # Right wrist
    [-0.3, 0.2],  # Left hand
    [-0.3, -0.2],  # Right hand
    [0, -0.5],  # Left knee
    [0, 0.5]  # Right knee
])

# Define the motion of the points
def motion(t):
    # Bowing motion
    bow_angle = np.pi / 2 * np.sin(t)
    return np.array([
        [0, 0],  # Head
        [0, -0.2],  # Left ear
        [0, 0.2],  # Right ear
        [-0.2 * np.cos(bow_angle), -0.1 * np.sin(bow_angle)],  # Left shoulder
        [-0.2 * np.cos(bow_angle), 0.1 * np.sin(bow_angle)],  # Right shoulder
        [0.2 * np.cos(bow_angle), -0.1 * np.sin(bow_angle)],  # Left hip
        [0.2 * np.cos(bow_angle), 0.1 * np.sin(bow_angle)],  # Right hip
        [-0.1 * np.cos(bow_angle), 0.3 * np.sin(bow_angle)],  # Left elbow
        [-0.1 * np.cos(bow_angle), -0.3 * np.sin(bow_angle)],  # Right elbow
        [0.1 * np.cos(bow_angle), 0.3 * np.sin(bow_angle)],  # Left wrist
        [0.1 * np.cos(bow_angle), -0.3 * np.sin(bow_angle)],  # Right wrist
        [-0.3 * np.cos(bow_angle), 0.2 * np.sin(bow_angle)],  # Left hand
        [-0.3 * np.cos(bow_angle), -0.2 * np.sin(bow_angle)],  # Right hand
        [0, -0.5 * np.cos(bow_angle)],  # Left knee
        [0, 0.5 * np.cos(bow_angle)]  # Right knee
    ])

# Create a new figure
fig, ax = plt.subplots()

# Set the background color
ax.set_facecolor(background_color)

# Initialize the plot with the first frame
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_axis_off()
points_plot, = ax.plot([], [], 'o', color=point_color)

# Function to update the plot for each frame
def update(t):
    points_data = motion(t)
    points_plot.set_data(points_data[:, 0], points_data[:, 1])
    return points_plot,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000 // frame_rate, blit=True)

# Show the animation
plt.show()
